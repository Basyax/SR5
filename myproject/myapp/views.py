from django.http import HttpResponse

def my_table(request):
    html = """
    <html>
    <head><title>Інформація про студента</title></head>
    <body style="font-family: Arial; margin: 40px;">
        <h2>Інформація про студента</h2>
        <table border="1" cellpadding="10" cellspacing="0">
            <tr><th>Поле</th><th>Значення</th></tr>
            <tr><td>Прізвище та ім’я</td><td>Овчаренко Владислав</td></tr>
            <tr><td>Група</td><td>КН-21</td></tr>
            <tr><td>Місто</td><td>Київ</td></tr>
            <tr><td>Університет</td><td>Ваш університет</td></tr>
        </table>
    </body>
    </html>
    """
    return HttpResponse(html)
