from django.shortcuts import render


def master(request):
    return render(request, 'master.html', {
        'it_companies': [
            {'title': 'Dell Technologies', 'id': 1},
            {'title': 'IBM', 'id': 2},
            {'title': 'Cisco Systems', 'id': 3}
        ]
    })


def detail(request, company_id):
    return render(request, 'detail.html', {
        'company_id': company_id
    })
