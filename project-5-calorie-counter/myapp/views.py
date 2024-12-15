from django.shortcuts import render, redirect
from myapp.models import Food, Consume

# Create your views here.
def index(request):
    if request.method == "POST":
        food_consumed_name = request.POST["food_consumed"]
        food_consumed = Food.objects.get(name=food_consumed_name)

        user = request.user
        consume = Consume(user=user,
                          food_consumed=food_consumed)
        consume.save()

    consumed_foods = Consume.objects.filter(user=request.user)
    foods = Food.objects.all()
    return render(request, 'myapp/index.html', {
        'foods': foods,
        'consumed_foods': consumed_foods,})

def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)

    if request.method == 'POST':
        consumed_food.delete()
        return redirect(index)

    return render(request, 'myapp/delete.html')

