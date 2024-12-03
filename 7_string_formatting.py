team1_num = 5
print('В команде Мастера кода участников: %s' % 5, '!')
team2_num = 6
print('Итого сегодня в командах участников: %s и  %s' % (5, 6), '!')
score_2 = 42
print('Команда Волшебники данных решила задач: {}'.format(score_2), '!')
team1_time = 18015.2
team2_time = 2153.31451
print('Команда Волшебники данных решили задачи за {}'.format(team1_time), 'c !')
score_1 = 40
print(f'Команды решили {score_1} и {score_2}' ' задач.')
challenge_result = 'Результат битвы: победа команды Мастера кода!'
print(f'{challenge_result}')
tasks_total = 82
time_avg = 350.4
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу !.')
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

print(result)