from django.shortcuts import render

# Index view with 7 days
def index(request):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return render(request, 'tasks/index.html', {'days': days})

# Day-specific task view
def day_view(request, day):
    tasks = {
        'Monday': ['Prepare for meetings'],
        'Tuesday': ['Grocery Shopping'],
        'Wednesday': ['Meeting with Mentor'],
        'Thursday': ['Read a Book'],
        'Friday': ['Code Practice', 'Movie Night'],
        'Saturday': ['Laundry', 'Relax'],
        'Sunday': ['Plan for Next Week']
    }
    return render(request, 'tasks/day.html', {'day': day, 'tasks': tasks.get(day, [])})
