from django.shortcuts import render
from .models import Bus, Stoppage, Next
from .forms import SearchForm
from django.http import JsonResponse

def home_view(request):
    return render(request, 'buses/home.html')

def search_view(request):
    form = SearchForm()

    return render(request, 'buses/search.html', {'form': form})

def ajax_stoppage(request):
    
    if request.is_ajax() and request.method == 'POST':
        stoppage = request.POST.get('stoppage', None)
        stoppages = Stoppage.objects.filter(name__icontains=stoppage)
        data = []
        
        for stoppage in stoppages:
            obj = dict(name = stoppage.name)
            data.append(obj)
        
        return JsonResponse({'data': data})
    
def ajax_search(request):
    
    if request.is_ajax() and request.method == 'POST':
        
        form = SearchForm(request.POST)
        
        if form.is_valid():
            s = form.cleaned_data['source']
            d = form.cleaned_data['destination']
            if(s==' '):
                print('sace')
        
            error1 = 0
            error2 = 0
            try:
                source = Stoppage.objects.get(name__iexact=s)
            except Stoppage.DoesNotExist:
                error1 = 1;

            try:
                destination = Stoppage.objects.get(name__iexact=d)
            except Stoppage.DoesNotExist:
                error2 = 1;

            #Source not found
            if error1 == 1 and error2 == 0:
                return JsonResponse({'error': 1})
            #Destination not found
            elif error1 == 0 and error2 == 1:
                return JsonResponse({'error': 2})
            #Both not found
            elif error1 == 1 and error2 == 1:
                return JsonResponse({'error': 3})
            #Both found
            else:
                buses1 = Bus.objects.filter(next__current=source).filter(next__next=destination)
                buses2 = Bus.objects.filter(next__current=destination).filter(next__next=source)
                buses = buses1.union(buses2)

                data = []

                for bus in buses:
                    obj = dict(pk = bus.pk, name = bus.name, start = bus.start.name, stop = bus.stop.name)
                    data.append(obj)

                return JsonResponse({'data': data, 'error': 0})

        else:
            return JsonResponse({'error': 4})
            
def buslist_view(request):
    buses = Bus.objects.all().order_by('name')
    
    return render(request, 'buses/buslist.html', {'buses': buses})

def busdetail_view(request, pk):
    bus = Bus.objects.get(pk=pk)
    pairs = Next.objects.filter(bus=bus)
    route = [ bus.start ]
    
    stoppage = bus.start
    while True:
        for pair in pairs:
            if pair.current == stoppage:
                route.append(pair.next)
                stoppage = pair.next
                break
        if stoppage == bus.stop:
            break
    
    return render(request, 'buses/busdetail.html', {'bus': bus, 'route': route})

def about_view(request):
    return render(request, 'buses/about.html')