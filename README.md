# NLP_yelp
## Determining the sentiment of review texts on the [YELP website](https://www.yelp.com/) / Определение тональности текстов отзывов на [сайте YELP](https://www.yelp.com/).

Цель: Созданию нейросети для определения тональности отзыва.

Результат: Создана нейросеть Lstm, которая была обучена на датасете отзывов yelp и была протестирована на собственном отзыве ресторана. Также было создано 2 нейросети с похожими результатами. Однако, их можно улучшить меняя гиперпараметры и кол-во эпох обучения.

Стек технологий: tensorflow, keras, pandas, numpy, matplotlib. Также была использована токенизация текста, а также функция callback для сохранения лучшей модели.

# График обучения нейросети lstm / Lstm neural network training schedule
![image](https://github.com/ArtemAvgutin/NLP_yelp/assets/131138862/8dde160c-42c6-42d8-bc37-35358faf5bac)

# График обучения одномерной сверточной сети/ Еraining schedule of a one-dimensional convolutional neural network
![image](https://github.com/ArtemAvgutin/NLP_yelp/assets/131138862/e8632833-e4ae-4e1e-9e28-fe86a0f4c507)

# Результат оценки собсвенного отзыва / The result of evaluating your own review
![image](https://github.com/ArtemAvgutin/NLP_yelp/assets/131138862/0e341135-e341-4356-b44e-75ec93ba1ff6)

Goal: Create a neural network to determine the sentiment of a review.

Result: The Lstm neural network was created, which was trained on the yelp review dataset and was tested on the restaurant’s own review. We also created 2 neural networks with similar results. However, they can be improved by changing the hyperparameters and the number of training epochs.

Technology stack: tensorflow, keras, pandas, numpy, matplotlib. Text tokenization was also used, as well as a callback function to save the best model.
