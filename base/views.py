
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadImageForm
from .predict import predict_image


def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            predicted_class = predict_image(image.image.path)
            image.predicted_class = predicted_class
            image.save()
            if predicted_class == 'EOSINOPHIL':
                characteristics = [
                    'Bi-lobed nucleus',
                    'Large orange-red granules in the cytoplasm',
                    'Involved in immune response against parasites',
                    'Approximately 2-5% of total white blood cells'
                ]
            elif predicted_class == 'LYMPHOCYTE':
                characteristics = [
                    'Round nucleus',
                    'Sparse cytoplasm',
                    'Key role in immune system defense',
                    'Approximately 20-40% of total white blood cells'
                ]
            elif predicted_class == 'MONOCYTE':
                characteristics = [
                    'Kidney-shaped nucleus',
                    'Abundant cytoplasm with fine granules',
                    'Differentiate into macrophages',
                    'Approximately 2-10% of total white blood cells'
                ]
            elif predicted_class == 'NEUTROPHIL':
                characteristics = [
                    'Multi-lobed nucleus',
                    'Pale granules in the cytoplasm',
                    'First responders to bacterial infection',
                    'Approximately 40-75% of total white blood cells'
                ]
            else:
                characteristics = ['No specific characteristics available']
            response_message = (
                f'<div class="card container">predicted class is <b class="txt-success">{predicted_class}.</b>'
                f'<br><b>Characteristics:</b> <ul>{"".join([f"<li>{char}</li>" for char in characteristics])}</ul></div>')

            return HttpResponse(response_message)

    else:
        form = UploadImageForm()

    return render(request, 'index.html', {'form': form})
