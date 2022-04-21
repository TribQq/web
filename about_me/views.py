# from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from .models import PortfolioSkillCard,PortfolioProjectCard


def about_main(request):
    return render(request, 'about_me_main.html')


def alt_about_me(request):
    return render(request, 'alt_about_me.html')


def portfolio_main(request):
    projects_cards = PortfolioProjectCard.objects.all().order_by('sort_index')
    skills_cards = PortfolioSkillCard.objects.all().order_by('sort_index')
    context = {'projects_cards': projects_cards, 'skills_cards': skills_cards}
    return render(request, 'portfolio_main.html', context=context)


def aeropack(request):
    """ http://www.aeropackbox.com/ """
    return render(request, 'portfolio/aeropack/aeropack_box.html')


def alapantan(request):
    return render(request, 'portfolio/alapantan/index.html')


def alapantan_basket(request):
    return render(request, 'portfolio/alapantan/basket.html')


def alapantan_buy(request):
    return render(request, 'portfolio/alapantan/buy.html')


def alapantan_card(request):
    return render(request, 'portfolio/alapantan/card.html')


def alapantan_catalog(request):
    return render(request, 'portfolio/alapantan/catalog.html')


def alapantan_checkout(request):
    return render(request, 'portfolio/alapantan/checkout.html')


def alapantan_checkout_1(request):
    return render(request, 'portfolio/alapantan/checkout-1.html')


def alapantan_checkout_2(request):
    return render(request, 'portfolio/alapantan/checkout-2.html')


def alapantan_checkout_3(request):
    return render(request, 'portfolio/alapantan/checkout-3.html')


def alapantan_checkout_4(request):
    return render(request, 'portfolio/alapantan/checkout-4.html')


def alapantan_checkout_5(request):
    return render(request, 'portfolio/alapantan/checkout-5.html')


def alapantan_delivery(request):
    return render(request, 'portfolio/alapantan/delivery.html')


def alapantan_loyality(request):
    return render(request, 'portfolio/alapantan/loyality.html')


def alapantan_modals(request):
    return render(request, 'portfolio/alapantan/modals.html')


def alapantan_news(request):
    return render(request, 'portfolio/alapantan/news.html')


def alapantan_payment(request):
    return render(request, 'portfolio/alapantan/payment.html')


def alapantan_personal_area(request):
    return render(request, 'portfolio/alapantan/personal_area.html')


def alapantan_question(request):
    return render(request, 'portfolio/alapantan/question.html')


def photo_birds(request):
    return render(request, 'portfolio/photo_birds/photo_birds.html')


def handler_404(request):
    """ page for 404 error"""
    return render(request, 'handlers/404.html')
