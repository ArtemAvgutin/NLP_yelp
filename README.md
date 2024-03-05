# NLP_yelp
## Determining the sentiment of review texts on the YELP website
## Определение тональности текстов отзывов на сайте YELP

* Работа по созданию нейросети для определения тональности отзыва. Создана нейросеть Lstm, которая была обучена на датасете отзывов yelp и была протестирована на собственном отзыве ресторана.
* Была использована токенизация текста, а также функция callback для сохранения лучшей модели. Также задача была решена одномерной сверточной сетью и было произведено сравнение результатов
* В результате работы было создано 2 нейросети с похожими результатами. Однако, их можно улучшить меняя гиперпараметры и кол-во эпох обучения.
# График обучения нейросети lstm / Lstm neural network training schedule
![image](https://github.com/ArtemAvgutin/NLP_yelp/assets/131138862/8dde160c-42c6-42d8-bc37-35358faf5bac)

# График обучения одномерной сверточной сети/ Еraining schedule of a one-dimensional convolutional neural network
![image](https://github.com/ArtemAvgutin/NLP_yelp/assets/131138862/e8632833-e4ae-4e1e-9e28-fe86a0f4c507)

# Результат оценки собсвенного отзыва / The result of evaluating your own review
![image](https://github.com/ArtemAvgutin/NLP_yelp/assets/131138862/0e341135-e341-4356-b44e-75ec93ba1ff6)

## В результате работы было создано 2 нейросети с похожими результатами. Однако, их можно улучшить меняя гиперпараметры и кол-во эпох обучения.
* Work on creating a neural network to determine the sentiment of a review. The Lstm neural network was created, which was trained on the Yelp review dataset and was tested on the restaurant’s own review.
* Text tokenization was used, as well as a callback function to save the best model. The problem was also solved with a one-dimensional convolutional network and the results were compared.
* As a result of the work, 2 neural networks were created with similar results. However, they can be improved by changing the hyperparameters and the number of training epochs.
