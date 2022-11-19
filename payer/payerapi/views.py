import os

from django.views.generic import TemplateView, View
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect
import stripe

from .models import Item, Order

stripe.api_key = os.environ.get('SECRET_API_KEY')


class BuyOrder(View):
    def get(self, request, pk):
        order = Order.objects.get(pk=pk)
        items_id = [item['id'] for item in order.items.values()]
        items = Item.objects.filter(pk__in=items_id).all()
        items_data = []

        for item in items:
            data = {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': int(item.price * 100),
                },
                'quantity': 1,
            }
            items_data.append(data)

        params = {
            "line_items": items_data,
            "mode": "payment",
            "success_url": f'{request.build_absolute_uri("/")}',
            "cancel_url": f'{request.build_absolute_uri("/")}',
        }

        if order.discount:
            params['discounts'] = [{"coupon": stripe.Coupon.create(duration="once", percent_off=order.discount.size)}]

        session = stripe.checkout.Session.create(**params)

        return redirect(session.url)


class BuyItemView(View):
    def get(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': int(item.price * 100),
                },
                'quantity': 1,
            }
            ],
            mode='payment',
            success_url=f'{request.build_absolute_uri("/")}',
            cancel_url=f'{request.build_absolute_uri("/")}',
        )

        return JsonResponse({
            "sessionId": session.id,
        })


class ItemView(TemplateView):
    template_name = 'payerapi/item.html'

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        item = get_object_or_404(Item, pk=pk)

        context['item'] = item
        context['PUBLIC_API_KEY'] = os.environ.get('PUBLIC_API_KEY')
        return context


class IndexView(TemplateView):
    template_name = 'payerapi/index.html'
