## ОПИСАНИЕ ПРОЕКТА
Представьте, что вы работаете стажером в отделении регионального банка. Вы все также делаете запросы к базам данных и строите отчеты. Вы поймали себя на мысли, что представляли работу дата-саентиста совсем иначе…

И вот сегодня, когда вы уже были на пороге отчаяния, ваш начальник пришел к вам с долгожданной новостью. Будем строить модель!

“Отлично,” – думаете вы, – “наконец-то смогу заняться настоящей работой!”

## ЦЕЛЬ ПРОЕКТА
Построить скоринг модель для вторичных клиентов банка, которая бы предсказывала вероятность дефолта клиента.

### Первоначальная версия датасета:
- **client_id** - идентификатор клиента
- **education** - уровень образования
- **sex** - пол заемщика
- **age** - возраст заемщика
- **car** - флаг наличия автомобиля
- **car_type** - флаг автомобиля иномарки
- **decline_app_cnt** - количество отказанных прошлых заявок
- **good_work** - флаг наличия “хорошей” работы
- **bki_request_cnt** - количество запросов в БКИ
- **home_address** - категоризатор домашнего адреса
- **work_address** - категоризатор рабочего адреса
- **income** - доход заемщика
- **foreign_passport** - наличие загранпаспорта
- **sna** - связь заемщика с клиентами банка
- **first_time** - давность наличия информации о заемщике
- **score_bki** - скоринговый балл по данным из БКИ
- **region_rating** - рейтинг региона
- **app_date** - дата подачи заявки
- **default** - флаг дефолта по кредиту

## ОПИСАНИЕ ПРОДЕЛАННОЙ РАБОТЫ

1. Заполнены пропуски у признака **education** в зависимости от флага наличия хорошей работы.
2. Добавлен признак **days** - количество дней, прошедших с подачи первой заявки.
3. Для получения распределения приближенного к нормальному были логарифмированы следующие признаки:
- age
- decline_app_cnt
- bki_request_cnt
- income
4. Проверена корреляция числовых признаков
5. Бинарные признаки и признак **education** были закодированы с помощью LabelEncoder()
6. Проверена значимость непрерывных и категориальных признаков
7. Добавлены полиноминальные признаки второго рода и затем стандартизированы
8. Для категориальных признаков было применено dummi-кодирование
9. К модели была применена регуляризация 

Помимо этого были проведены тесты модели с:
- удалением объектов с пропусками
- удалением малозначимых признаков
- добавлением полиномиальных признаков 3-го и 4-го порядков
Однако поскольку тесты показали ухудшение метрик: ROC-AUC и confusion_matrix, - к финальному датасету эти преобразования применены не были. 

## РЕЗУЛЬТАТЫ
score - 0.73838
7 место из 42 на 10.10.20
