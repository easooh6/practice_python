import wikipedia

print(wikipedia.summary('Kazakhstan\n')) #Kazakhstan, officially the Republic of Kazakhstan, is a landlocked country primarily in Central Asia,
                                         #with a small portion in Eastern Europe. It borders Russia to the north and west, China to the east и так далее
print(wikipedia.search('Kazakhstan')) #['Kazakhstan', 'Economy of Kazakhstan', 'Demographics of Kazakhstan',
                                      #'Kazakhstan national football team', 'History of Kazakhstan', 'Astana'
                                      #  'Regions of Kazakhstan', 'Languages of Kazakhstan', 'Almaty', 'Flag of Kazakhstan']

wikipedia.set_lang('ru')
page = wikipedia.page('Almaty')

print(page.title) # Kazakhstan, officially the Republic of Kazakhstan, is a landlocked country primarily in Central Asia, with a small portion in Eastern Europe.
print(page.url) # https://ru.wikipedia.org/wiki/%D0%90%D0%BB%D0%BC%D0%B0-%D0%90%D1%82%D0%B0
print(page.content) # В советское время ведущим футбольным клубом Казахской ССР был алма-атинский «Кайрат». 
print(page.links) # '16 февраля', '1854', '1854 год', '1867', '1867 год', '1887 год', '1921 год', '2011 год в истории метрополитена', '23 апреля', '25 июля', '316-я стрелковая дивизия (1-го формирования)',