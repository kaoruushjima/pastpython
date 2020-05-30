from django.views.generic import View
from django.shortcuts import render, redirect
from django.urls import reverse

from bitly.models.bitlink import Bitlink


class BitlinkCreateView(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "bitly/new.html",
            context={},
        )

    def post(self, request, *args, **kwargs):
        original_url = request.POST.get("original_url")
        user = request.user

        bitlink = request.user.bitlink_set.create(
            original_url=original_url,
        )

        # bitlink.id => bitlink.shorten_hash  생성 (hash_id)
        bitlink.save()

        return redirect(reverse("home"))
