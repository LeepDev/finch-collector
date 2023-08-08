from django.shortcuts import render

finches = [
    { 'name': 'Finchy', 'color': 'blue', 'size': 'small'},
    { 'name': 'Frenchy', 'color': 'red', 'size': 'medium'},
    { 'name': 'Fry', 'color': 'yellow', 'size': 'large'},
]

# Create your views here.
def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', { 'finches': finches })