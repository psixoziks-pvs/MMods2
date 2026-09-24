# -*- coding: utf-8 -*-
"""PNecrome — единый источник таблиц (моб-ориентированная семантика).

Семантика скрещивания: берём ТРУП моба-донора X, выпиливаем из него часть тела P
и приживляем эту часть ЛЮБОМУ живому мобу. Гибрид наследует базовый тип жертвы
(её поведение), а имя и статы задаются этой таблицей по донору.
"""

VERSIONS = {
    'forge-1.16.5':  dict(mc='1.16.5', forge='36.2.39', loader_range='[36,)',     java=8),
    'forge-1.18.2':  dict(mc='1.18.2', forge='40.2.0',  loader_range='[38,41)',   java=17),
    'forge-1.19.2':  dict(mc='1.19.2', forge='43.3.13', loader_range='[41,44)',   java=17),
    'forge-1.20.1':  dict(mc='1.20.1', forge='47.2.0',  loader_range='[47,48)',   java=17),
    'neoforge-1.21': dict(mc='1.21',   forge='21.0.37', loader_range='[21.0,22)', java=21),
}

PARTS = ['head', 'arms', 'legs', 'torso']
MODID = 'pnecrome'

DONOR_RU = {
    'zombie': u'зомби',
    'creeper': u'крипера',
    'skeleton': u'скелета',
    'spider': u'паука',
    'cave_spider': u'пещерного паука',
    'enderman': u'эндермена',
    'blaze': u'блаза',
    'witch': u'ведьмы',
    'villager': u'жителя',
    'iron_golem': u'железного голема',
    'pig': u'свиньи',
    'cow': u'коровы',
    'sheep': u'овцы',
    'chicken': u'курицы',
    'horse': u'лошади',
    'wolf': u'волка',
    'ocelot': u'оцелота',
    'cat': u'кошки',
    'goat': u'козла',
    'panda': u'панды',
    'fox': u'лисы',
    'bee': u'пчелы',
    'dolphin': u'дельфина',
    'axolotl': u'аксолотля',
    'turtle': u'черепахи',
    'cod': u'трески',
    'salmon': u'лосося',
    'tropical_fish': u'тропической рыбы',
    'pufferfish': u'рыбы-фугу',
    'mooshroom': u'муушома',
    'squid': u'кальмара',
    'glow_squid': u'светящегося кальмара',
    'bat': u'летучей мыши',
    'parrot': u'попугая',
    'rabbit': u'кролика',
    'frog': u'лягушки',
    'camel': u'верблюда',
    'sniffer': u'нюхача',
    'husk': u'мумии',
    'drowned': u'утопленника',
    'stray': u'снежного скелета',
    'mule': u'мула',
    'donkey': u'осла',
    'llama': u'ламы',
    'trader_llama': u'торговой ламы',
    'polar_bear': u'белого медведя',
    'piglin': u'пиглина',
    'piglin_brute': u'пиглина-брутала',
    'hoglin': u'хоглина',
    'zoglin': u'зоглина',
    'zombified_piglin': u'зомбифицированного пиглина',
    'wither_skeleton': u'иссушителя',
    'snow_golem': u'снежного голема',
    'giant': u'гиганта',
    'phantom': u'фантома',
    'zombie_villager': u'зомби-жителя',
    'silverfish': u'чешуйницы',
    'endermite': u'эндермита',
    'vex': u'векса',
    'evoker': u'заклинателя',
    'vindicator': u'ревнителя',
    'illusioner': u'иллюзиониста',
    'pillager': u'разбойника',
    'ravager': u'разорителя',
    'warden': u'наказателя',
    'breeze': u'бриза',
    'slime': u'слизня',
    'magma_cube': u'магмового куба',
    'ghast': u'гаста',
    'shulker': u'шалкера',
    'guardian': u'стража',
    'elder_guardian': u'древнего стража',
}

# ---------------------------------------------------------------------
# Таблица гибридов: donor | part | id | name_ru | name_en | hp | spd | dmg | fire | desc
# ---------------------------------------------------------------------
HYBRIDS_RAW = u'''
zombie|head|revenant|Ревенант|Revenant|1.5|1.0|1.5|false|Ожившая голова зомби: бьёт жадно и не знает покоя.
zombie|arms|graspulo|Хватун|Graspulo|1.0|1.0|1.5|false|Руки зомби хватают мёртвой хваткой.
zombie|legs|shambler|Хромоступ|Shambler|1.0|0.9|1.0|false|Походку ходячего мертвеца не остановить.
zombie|torso|carrionkin|Мертвецовина|Carrionkin|1.5|1.0|1.0|false|Туша, что кормит сама себя.
creeper|head|miasma|Миазма|Miasma|1.0|1.1|1.0|false|Шипящий череп, пропитанный порохом.
creeper|arms|fusearm|Детонатор|Fusearm|1.0|1.0|1.0|false|Обнимает — и шипит.
creeper|legs|hissstride|Шипоход|Hissstride|1.0|1.2|1.0|false|Крадётся, тихо шипя на каждый шаг.
creeper|torso|blisterhide|Пузырешкура|Blisterhide|1.0|1.0|1.0|false|Кожа вздулась порохом.
skeleton|head|bonewraith|Костяной призрак|Bonewraith|1.0|1.0|1.0|false|Пустой череп, в котором горит холодный огонь.
skeleton|arms|bonewrist|Кистекость|Bonewrist|1.0|1.0|1.0|false|Ловкий запястный хват из чистых костей.
skeleton|legs|boneshanks|Костоплёт|Boneshanks|1.0|1.2|1.0|false|Стучат в гроб изнутри.
skeleton|torso|ribcage|Реброклон|Ribcage|1.0|1.0|1.0|false|Грудная клетка, созвучная арфе смерти.
spider|head|weaver|Ткач|Weaver|1.0|1.2|1.0|false|Восемь глаз смотрят из-под савана.
spider|arms|legsworn|Паучелап|Legsworn|1.0|1.1|1.0|false|Восемь рук вместо двух.
spider|legs|skitterling|Скиттерлинг|Skitterling|1.0|1.5|1.0|false|Восемь шагов на один вдох.
spider|torso|fuzzback|Пухоспин|Fuzzback|1.0|1.0|1.0|false|Мохнатая спина выползает из щели.
cave_spider|head|venomweaver|Ядовитый ткач|Venomweaver|1.0|1.2|1.0|false|Его взгляд обжигает плоть ядом.
cave_spider|arms|venomclutch|Ядохват|Venomclutch|1.0|1.0|1.0|false|Обнимает и заражает.
cave_spider|legs|creepskitter|Ползунок|Creepskitter|1.0|1.4|1.0|false|Тихо крадётся по стенам.
cave_spider|torso|greenscab|Зелёная парша|Greenscab|1.0|1.0|1.0|false|Бока, сочащиеся ядом.
enderman|head|hollow|Пустотелый|Hollow|1.5|1.1|1.5|false|Не смотрите ему в глаза... если они ещё есть.
enderman|arms|voidreach|Пустотомах|Voidreach|1.0|1.0|1.5|false|Достаёт оттуда, откуда не возвращаются.
enderman|legs|longstride|Дальноход|Longstride|1.0|1.5|1.0|false|Шаг — и его уже нет.
enderman|torso|portalhide|Портальник|Portalhide|1.5|1.0|1.0|false|В рёбрах его груди гаснут миры.
blaze|head|emberwight|Уголёк|Emberwight|1.0|1.0|1.5|true|Тлеющий череп из загробного пламени.
blaze|arms|embergrasp|Углохват|Embergrasp|1.0|1.0|1.5|true|Рукавицы из жара.
blaze|legs|firewalk|Огнеход|Firewalk|1.0|1.2|1.0|true|Стебли пламени вместо ног.
blaze|torso|cinderchest|Углескул|Cinderchest|1.0|1.0|1.0|true|Грудная клетка из пылающих прутьев.
witch|head|hexling|Ведьмёныш|Hexling|1.0|1.0|1.0|false|Маленький наводчик порчи.
witch|arms|cauldronarms|Котелкорук|Cauldronarms|1.0|1.0|1.0|false|Мешает варево из теней.
witch|legs|hextrip|Ведрога|Hextrip|1.0|1.1|1.0|false|Спотыкаешься там, где она прошла.
witch|torso|brewhide|Варешкура|Brewhide|1.0|1.0|1.0|false|Пахнет полынью и серой.
villager|head|curseling|Проклятор|Curseling|1.0|1.0|1.0|false|Житель, чья душа осталась в трупе.
villager|arms|traderhands|Торговец|Traderhands|1.0|1.0|1.0|false|Продаёт то, чего нет.
villager|legs|marketstrider|Базарник|Marketstrider|1.0|1.1|1.0|false|Ходит рядами пустых лавок.
villager|torso|toadycloth|Ряба|Toadycloth|1.0|1.0|1.0|false|Роба торговца, снятая с живого.
iron_golem|head|dreadnought|Грозобор|Dreadnought|2.0|0.9|1.5|false|Железная голова, что помнит долг стража.
iron_golem|arms|ironmaul|Железнобой|Ironmaul|2.0|0.9|2.0|false|Удар молота из кованого металла.
iron_golem|legs|bulwark|Бастион|Bulwark|2.0|0.8|1.0|false|Ноги из крепостной стены.
iron_golem|torso|platebelly|Брюхолит|Platebelly|2.0|1.0|1.0|false|Живот из клёпаного железа.
pig|head|grunkgul|Хрюкогуль|Grunkgul|1.0|1.0|1.0|false|Хрюкает из-за гроба и всё ещё ведёт на убой.
pig|arms|trotterarms|Копытерук|Trotterarms|1.0|1.0|1.0|false|Копыта вместо ладоней.
pig|legs|trotter|Бегоножка|Trotter|1.0|1.3|1.0|false|Трусит к бойне сама.
pig|torso|baconhide|Салошкура|Baconhide|1.0|1.0|1.0|false|Сало, что не берёт нож.
cow|head|mooreshade|Мычатень|Mooreshade|1.0|1.0|1.0|false|Тень рогатого пастбища.
cow|arms|milktouch|Молокоперст|Milktouch|1.0|1.0|1.0|false|Ласковое доитьё.
cow|legs|taurokk|Таурокк|Taurokk|1.5|1.2|1.0|false|Бычьи ноги несут быстрее боли.
cow|torso|beefside|Говядобок|Beefside|1.0|1.0|1.0|false|Сочное мясо, что не портится.
sheep|head|fleeceghast|Рунопризрак|Fleeceghast|1.0|1.0|1.0|false|Шерсть, что шевелится сама.
sheep|arms|fleecemittens|Шерстолапка|Fleecemittens|1.0|1.0|1.0|false|Мягкие, но цепкие.
sheep|legs|woolwalker|Шерстеход|Woolwalker|1.0|1.1|1.0|false|Топает мягко, как снег.
sheep|torso|fleecybod|Рунобрюх|Fleecybod|1.0|1.0|1.0|false|Брюхо тёплое, как могила зимой.
chicken|head|clatterhen|Клакуша|Clatterhen|1.0|1.2|1.0|false|Несёт только яйца из костей.
chicken|arms|wingreach|Крылкорук|Wingreach|1.0|1.0|1.0|false|Крылья вместо рук.
chicken|legs|scratchling|Царапун|Scratchling|1.0|1.3|1.0|false|Роет могилы когтями.
chicken|torso|featherpelt|Перешкур|Featherpelt|1.0|1.0|1.0|false|Щипаная тушка, что встала сама.
horse|head|nightmare|Кошмар|Nightmare|1.0|1.3|1.0|false|Скачет там, где нет дороги.
horse|arms|hoofgauntlet|Кованорука|Hoofgauntlet|1.0|1.0|1.0|false|Подкова в кулаке.
horse|legs|striderspawn|Странник|Striderspawn|1.0|1.5|1.0|false|Копыта, что не знают устали.
horse|torso|barrelbred|Бочкогрив|Barrelbred|1.0|1.0|1.0|false|Широкая грудь для скачки в вечность.
wolf|head|grimfang|Мрачнозуб|Grimfang|1.0|1.2|1.5|false|Верный пёс даже после смерти.
wolf|arms|clutchjaw|Хваткогель|Clutchjaw|1.0|1.0|1.5|false|Держит мёртвой хваткой.
wolf|legs|dashhound|Погонщик|Dashhound|1.0|1.5|1.0|false|Догоняет даже убегающую жизнь.
wolf|torso|sheltere|Шерстозвер|Sheltere|1.0|1.0|1.0|false|Грубая шерсть сторожевого пса.
ocelot|head|shadowprowler|Тенеброд|Shadowprowler|1.0|1.3|1.0|false|Бесшумный охотник сумрака.
ocelot|arms|softtalons|Мягкий коготь|Softtalons|1.0|1.0|1.0|false|Царапает без звука.
ocelot|legs|silkpaw|Шелколап|Silkpaw|1.0|1.5|1.0|false|Лапа тише шёлка.
ocelot|torso|junglecoat|Джунглеплащ|Junglecoat|1.0|1.0|1.0|false|Пятнистая шкура джунглей.
cat|head|nineveil|Девятизавес|Nineveil|1.0|1.2|1.0|false|Все девять жизней ушли в тенета.
cat|arms|silkscratch|Шелкодрать|Silkscratch|1.0|1.0|1.0|false|Оставляет пять борозд.
cat|legs|velvetclaw|Бархатный коготь|Velvetclaw|1.0|1.5|1.0|false|Приземляется всегда на ту сторону.
cat|torso|ashpelt|Пеплошкура|Ashpelt|1.0|1.0|1.0|false|Серая шерсть, пахнущая гарью.
goat|head|ramshorn|Рогочаст|Ramshorn|1.0|1.1|1.5|false|Бодает призрачные горы.
goat|arms|ramshoulder|Баранье плечо|Ramshoulder|1.0|1.0|1.5|false|Плечо, что сносит двери.
goat|legs|scraphooves|Сквозкопыт|Scraphooves|1.0|1.3|1.0|false|Бьёт копытом о камень склепа.
goat|torso|mountainmane|Горногрив|Mountainmane|1.0|1.0|1.0|false|Грива, пахнущая камнем и солью.
panda|head|bamboogul|Бамбукогуль|Bamboogul|1.5|0.9|1.0|false|Сонный гигант бамбуковых склепов.
panda|arms|bamboohug|Бамбуконятие|Bamboohug|1.5|1.0|1.0|false|Объятия тяжёлые, как ствол.
panda|legs|reedshambler|Тростник-ходунок|Reedshambler|1.0|0.9|1.0|false|Идёт медленно, но верно.
panda|torso|bambooloam|Бамбукслизь|Bambooloam|1.5|1.0|1.0|false|Толокно из сонной бамбуковой пыли.
fox|head|vulpine|Лисолюд|Vulpine|1.0|1.3|1.0|false|Хитёр и после погоста.
fox|arms|slypaws|Лиселипы|Slypaws|1.0|1.0|1.0|false|Крадёт из-под носа.
fox|legs|quickvein|Быстрожил|Quickvein|1.0|1.4|1.0|false|Лисий бег по тонкому льду.
fox|torso|emberfur|Уголемех|Emberfur|1.0|1.0|1.0|false|Рыжий мех, тлеющий изнутри.
bee|head|stinger|Жалинг|Stinger|1.0|1.2|1.0|false|Жужжание из-под земли.
bee|arms|stingarms|Жалкорук|Stingarms|1.0|1.0|1.0|false|Обнимает и жалит.
bee|legs|pollenghast|Пыльцемер|Pollenghast|1.0|1.3|1.0|false|Собирает пыль с надгробий.
bee|torso|fuzzbum|Пухозад|Fuzzbum|1.0|1.0|1.0|false|Пушистый зад, гудящий на весь улей.
dolphin|head|tidesoul|Приливник|Tidesoul|1.0|1.2|1.0|false|Дельфин, заплывший в мир мёртвых.
dolphin|arms|flippergrasp|Ластохват|Flippergrasp|1.0|1.0|1.0|false|Ласты, что топят.
dolphin|legs|swiftcurrent|Быстротечение|Swiftcurrent|1.0|1.4|1.0|false|Течёт против смерти.
dolphin|torso|waveside|Волнобок|Waveside|1.0|1.0|1.0|false|Гладкий бок, режущий волну.
axolotl|head|gillfiend|Жабролюд|Gillfiend|1.0|1.1|1.0|false|Улыбается, даже будучи мертвецом.
axolotl|arms|gillhold|Жаброхват|Gillhold|1.0|1.0|1.0|false|Хватает за жабры.
axolotl|legs|marshskipper|Топебол|Marshskipper|1.0|1.2|1.0|false|Перебирается через топи.
axolotl|torso|gillmass|Жаберник|Gillmass|1.0|1.0|1.0|false|Пучок алых жабр на боку.
turtle|head|shellwarden|Панцирник|Shellwarden|1.5|0.8|1.0|false|Дом, который пережил хозяина.
turtle|arms|flippershield|Ластощит|Flippershield|1.5|1.0|1.0|false|Отбивает удары панцирем.
turtle|legs|tidecrawler|Приливополз|Tidecrawler|1.0|0.9|1.0|false|Ползёт к морю мертвецов.
turtle|torso|scuteplate|Щитоспин|Scuteplate|1.5|1.0|1.0|false|Панцирные пластины старого моряка.
cod|head|scalespawn|Чешуйник|Scalespawn|1.0|1.0|1.0|false|Мелкая рыбья нежить.
cod|arms|finclasp|Плавнехват|Finclasp|1.0|1.0|1.0|false|Скользкий захват.
cod|legs|finsteps|Плавненога|Finsteps|1.0|1.1|1.0|false|Плавает по суше, как по воде.
cod|torso|silverflank|Серебробок|Silverflank|1.0|1.0|1.0|false|Чешуя блестит, как монета утопленника.
salmon|head|runsire|Нерестник|Runsire|1.0|1.0|1.0|false|Идёт против течения смерти.
salmon|arms|rivergrab|Речной захват|Rivergrab|1.0|1.0|1.0|false|Тянет в воду.
salmon|legs|riverdash|Речной бегун|Riverdash|1.0|1.3|1.0|false|Прыгает через плотину стужи.
salmon|torso|runside|Нерестебок|Runside|1.0|1.0|1.0|false|Бока красные от дальней дороги.
tropical_fish|head|coralgul|Коралкогуль|Coralgul|1.0|1.0|1.0|false|Яркий, как закат над могилой.
tropical_fish|arms|coralgrasp|Кораллохват|Coralgrasp|1.0|1.0|1.0|false|Царапает, как риф.
tropical_fish|legs|reefling|Рифлик|Reebling|1.0|1.1|1.0|false|Пёстрый малёк глубин.
tropical_fish|torso|reefbelly|Рифопуз|Reefbelly|1.0|1.0|1.0|false|Расписное брюхо тёплых вод.
pufferfish|head|bloatling|Надутыш|Bloatling|1.0|1.0|1.0|false|Надувается от собственного яда.
pufferfish|arms|spikehug|Колючие объятья|Spikehug|1.0|1.0|1.0|false|Обнимешь — пожалеешь.
pufferfish|legs|spikestand|Колючестое|Spikestand|1.0|0.9|1.0|false|Стоит на иголках.
pufferfish|torso|bloatbod|Раздутень|Bloatbod|1.0|1.0|1.0|false|Надутое тело, полное воздуха и яда.
mooshroom|head|capghast|Шляпопризрак|Capghast|1.0|1.0|1.0|false|Грибница, проросшая сквозь череп.
mooshroom|arms|capembrace|Шляпопонятие|Capembrace|1.0|1.0|1.0|false|Тепло гнилых грибов.
mooshroom|legs|myceliamble|Грибоход|Myceliamble|1.0|1.0|1.0|false|За ним растёт грибница.
mooshroom|torso|shroomhide|Грибошкура|Shroomhide|1.0|1.0|1.0|false|Кожа, усеянная шляпками мухоморов.
squid|head|inkshade|Чернильник|Inkshade|1.0|1.0|1.0|false|Окрашивает туман в чёрный.
squid|arms|tentaclemass|Щупальщик|Tentaclemass|1.0|1.0|1.0|false|Опутывает всего.
squid|legs|tentaclelimb|Щупаленог|Tentaclelimb|1.0|1.1|1.0|false|Хватает за ногу из темноты.
squid|torso|blackbile|Черножелчь|Blackbile|1.0|1.0|1.0|false|Мешочки с чернилами под рёбрами.
glow_squid|head|lanternsquid|Фонароголь|Lanternsquid|1.0|1.0|1.0|false|Свет маяка для заблудших душ.
glow_squid|arms|lampclutch|Светохват|Lampclutch|1.0|1.0|1.0|false|Светящиеся наручники.
glow_squid|legs|glowtentacle|Светощуп|Glowtentacle|1.0|1.1|1.0|false|Фонари из щупалец.
glow_squid|torso|lumenbelly|Светопуз|Lumenbelly|1.0|1.0|1.0|false|Брюхо, светящееся в толще воды.
bat|head|nightwing|Ночнокрыл|Nightwing|1.0|1.2|1.0|false|Крик летучей мыши из склепа.
bat|arms|batwingarms|Нетопылерук|Batwingarms|1.0|1.0|1.0|false|Обвивает, как плащ.
bat|legs|roosthang|Нетылыш|Roosthang|1.0|1.2|1.0|false|Висит вниз головой вечно.
bat|torso|hangpelt|Подвесшкур|Hangpelt|1.0|1.0|1.0|false|Шкурка, привыкшая висеть вверх ногами.
parrot|head|plumeclaw|Пернокоть|Plumeclaw|1.0|1.1|1.0|false|Повторяет последние слова умерших.
parrot|arms|feathergrip|Перахват|Feathergrip|1.0|1.0|1.0|false|Щекотно и больно.
parrot|legs|perchling|Жердочник|Perchling|1.0|1.2|1.0|false|Цепляется за любую ветку.
parrot|torso|plumebod|Перотело|Plumebod|1.0|1.0|1.0|false|Оперение шуршит, как страницы книги.
rabbit|head|thumpkin|Топотун|Thumpkin|1.0|1.4|1.0|false|Стучит лапами из-под плиты.
rabbit|arms|thumpfists|Топот-кулаки|Thumpfists|1.0|1.0|1.0|false|Бьёт лапой наотмашь.
rabbit|legs|hoppyghast|Прыгун-призрак|Hoppyghast|1.0|1.5|1.0|false|Скачет выше забора кладбища.
rabbit|torso|softdown|Пухотело|Softdown|1.0|1.0|1.0|false|Мягкий подшёрсток быстрой жертвы.
frog|head|marshcroaker|Топотун топей|Marshcroaker|1.0|1.1|1.0|false|Квакает на болотах душ.
frog|arms|stickytoes|Липкопальцы|Stickytoes|1.0|1.0|1.0|false|Присоски на костяшках.
frog|legs|leaper|Прыткотоп|Leaper|1.0|1.4|1.0|false|Лягушачий прыжок в вечность.
frog|torso|mudbelly|Грязепуз|Mudbelly|1.0|1.0|1.0|false|Влажное брюхо, надувающееся перед прыжком.
camel|head|caravangul|Каравангуль|Caravangul|1.5|1.1|1.0|false|Везёт караван из преисподней.
camel|arms|humpguard|Горбохват|Humpguard|1.5|1.0|1.0|false|Держится за горб крепко.
camel|legs|dunestrider|Дюноход|Dunestrider|1.0|1.4|1.0|false|Идёт по барханам забвения.
camel|torso|humpside|Горбобок|Humpside|1.5|1.0|1.0|false|Горбы полны воды для долгого пути.
sniffer|head|gravehunter|Могильный пёс|Gravehunter|1.0|1.1|1.0|false|Чует семена древних кладбищ.
sniffer|arms|snoutdigger|Нюхокоп|Snoutdigger|1.0|1.0|1.0|false|Роет носом и руками.
sniffer|legs|rootsnatcher|Корнеед|Rootsnatcher|1.0|1.1|1.0|false|Вынюхивает корни под плитой.
sniffer|torso|rootfur|Корнешерсть|Rootfur|1.0|1.0|1.0|false|Шерсть, спутанная с корнями древних трав.
husk|head|dustwight|Пылепризрак|Dustwight|1.0|1.0|1.0|true|Высох в песках времени.
husk|arms|sandgrip|Пескохват|Sandgrip|1.0|1.0|1.0|true|Сушит кожу одним касанием.
husk|legs|dusttreader|Пылемер|Dusttreader|1.0|1.1|1.0|true|Шаг — и песок шепчет имя.
husk|torso|deshide|Пустынкошкура|Deshide|1.0|1.0|1.0|true|Кожа, дублёная песком и солнцем.
drowned|head|brinewight|Солончег|Brinewight|1.0|1.0|1.0|false|Пропитан морской солью и тлением.
drowned|arms|webhand|Сетерук|Webhand|1.0|1.0|1.0|false|Скользок, как угорь.
drowned|legs|kelpshanks|Водорослег|Kelpshanks|1.0|1.1|1.0|false|Пахнут тиной и могилой.
drowned|torso|kelpbelly|Водорослебрюх|Kelpbelly|1.0|1.0|1.0|false|Живот, обросший подводной травой.
stray|head|frostbone|Инеекость|Frostbone|1.0|1.0|1.0|false|Стреляет инеем из-за могилы.
stray|arms|frostgrip|Инехват|Frostgrip|1.0|1.0|1.0|false|Рукавичка из инея.
stray|legs|iceshanks|Леденог|Iceshanks|1.0|1.1|1.0|false|Хрустят, как наст.
stray|torso|frostpelt|Инешкура|Frostpelt|1.0|1.0|1.0|false|Шкура, покрытая изморозью.
mule|head|packdead|Пакорок|Packdead|1.0|1.0|1.0|false|Вьючное животное загроба.
mule|arms|packreach|Вьюкорук|Packreach|1.0|1.0|1.0|false|Натянет вьюк на кого угодно.
mule|legs|burdenbeast|Тяглек|Burdenbeast|1.0|1.1|1.0|false|Несёт ношу мёртвых.
mule|torso|packsaddle|Вьюкож|Packsaddle|1.0|1.0|1.0|false|Спина, помнящая вьюки.
donkey|head|millergul|Мельник|Millergul|1.0|1.0|1.0|false|Мелет кости в муку.
donkey|arms|quernarm|Жерноворук|Quernarm|1.0|1.0|1.0|false|Крутит жернова из костей.
donkey|legs|panniershade|Понузник|Panniershade|1.0|1.1|1.0|false|Вьюки полны костей.
donkey|torso|millhide|Мельничная кожа|Millhide|1.0|1.0|1.0|false|Шкура, пропахшая мукой и костной пылью.
llama|head|woolphantom|Шерстофантом|Woolphantom|1.0|1.0|1.0|false|Плевётся призрачной шерстью.
llama|arms|spitguard|Плевок|Spitguard|1.0|1.0|1.0|false|Плюёт наглой слюной.
llama|legs|caravanstep|Караванный шаг|Caravanstep|1.0|1.1|1.0|false|Идёт вереницей за горизонт.
llama|torso|woolmass|Шерстогруз|Woolmass|1.0|1.0|1.0|false|Клубок шерсти, что несёт ношу.
trader_llama|head|bazaarwraith|Базарный призрак|Bazaarwraith|1.0|1.0|1.0|false|Торгует редкостями мертвецов.
trader_llama|arms|bellsleeve|Бубенец|Bellsleeve|1.0|1.0|1.0|false|Рукав с бубенцами идущего каравана.
trader_llama|legs|peddler|Холак|Peddler|1.0|1.2|1.0|false|Разносит товар меж миров.
trader_llama|torso|saddleside|Седлобок|Saddleside|1.0|1.0|1.0|false|Бока, отёртые купеческим седлом.
polar_bear|head|icepaw|Ледопал|Icepaw|1.5|1.0|1.5|false|Хищник белых пустошей.
polar_bear|arms|sealfist|Тюленекулак|Sealfist|1.0|1.0|1.5|false|Бьёт лапой, как об лёд.
polar_bear|legs|floetracker|Ледоход|Floetracker|1.0|1.2|1.0|false|Ходит по тонкой корке могил.
polar_bear|torso|blizzardcoat|Буранник|Blizzardcoat|1.5|1.0|1.0|false|Шкура, сшитая из метели.
piglin|head|goldghast|Златожаба|Goldghast|1.0|1.0|1.5|false|Жадность пережила смерть.
piglin|arms|goldcuff|Златоноша|Goldcuff|1.0|1.0|1.5|false|Наручи из слитков.
piglin|legs|coinrunner|Монетоход|Coinrunner|1.0|1.2|1.0|false|Бегает за золотом в ад.
piglin|torso|giltbelly|Златобрюх|Giltbelly|1.0|1.0|1.0|false|Пузо, отполированное монетами.
piglin_brute|head|bruteshade|Отверженный|Bruteshade|1.5|1.0|2.0|false|Кулак, который не гнётся.
piglin_brute|arms|axearm|Секирорука|Axearm|1.5|1.0|2.0|false|Одна рука — один удар.
piglin_brute|legs|banishedpace|Ссылбег|Banishedpace|1.0|1.2|1.0|false|Бежит туда, откуда не возвращаются.
piglin_brute|torso|brutemail|Грубоброня|Brutemail|1.5|1.0|1.5|false|Кожаный панцирь арены.
hoglin|head|tuskfiend|Клыкостраф|Tuskfiend|1.5|1.1|1.5|false|Рыщет по багровым лесам.
hoglin|arms|tuskgrip|Клыкохват|Tuskgrip|1.0|1.0|1.5|false|Загнул клыки на руки.
hoglin|legs|rooter|Корнебой|Rooter|1.0|1.2|1.0|false|Выворачивает землю копытом.
hoglin|torso|truffleskin|Трюфелешкур|Truffleskin|1.5|1.0|1.0|false|Кожа, пропахшая подземными грибами.
zoglin|head|rotstalker|Гнилоход|Rotstalker|1.5|1.1|1.5|false|Зомбированный кабан ада.
zoglin|arms|rotclaw|Гнилокоготь|Rotclaw|1.0|1.0|1.5|false|Царапает до лихорадки.
zoglin|legs|rottrotter|Гнилобег|Rottrotter|1.0|1.3|1.0|false|Бежит, оставляя вонь.
zoglin|torso|putridheave|Смердосвал|Putridheave|1.5|1.0|1.0|false|Туша, от которой стелется смрад.
zombified_piglin|head|emberbaron|Угольный барон|Emberbaron|1.5|1.0|1.5|true|Держит суд над угольем.
zombified_piglin|arms|embergauntlet|Угольная рукавица|Embergauntlet|1.0|1.0|1.5|true|Рукавица из углей.
zombified_piglin|legs|emberstrider|Уголовник|Emberstrider|1.0|1.1|1.0|true|Идёт по углям, как по траве.
zombified_piglin|torso|scorchbelly|Подчрево|Scorchbelly|1.5|1.0|1.0|true|Брюхо, запечённое в аду.
wither_skeleton|head|charredlord|Обугленный лорд|Charredlord|1.5|1.0|2.0|true|Лорд иссушенных земель.
wither_skeleton|arms|withergrasp|Иссухохват|Withergrasp|1.5|1.0|2.0|true|Касание — иссушение.
wither_skeleton|legs|ashwalker|Пепелеход|Ashwalker|1.0|1.1|1.0|true|Не оставляет следа на пепле.
wither_skeleton|torso|charribone|Углекость|Charribone|1.5|1.0|1.5|true|Рёбра, обугленные в адовых печах.
snow_golem|head|rimeguard|Инейный страж|Rimeguard|1.0|1.0|1.0|false|Страж снежных склепов.
snow_golem|arms|snowfling|Снежнелёт|Snowfling|1.0|1.0|1.0|false|Метает комья вечной мерзлоты.
snow_golem|legs|driftwalker|Снегоброд|Driftwalker|1.0|1.1|1.0|false|Оставляет след из изморози.
snow_golem|torso|slushcore|Слякотяж|Slushcore|1.0|1.0|1.0|false|Сердцевина из тающего снега.
giant|head|titanmaw|Титанья пасть|Titanmaw|2.0|1.0|2.0|false|Челюсти забытого исполина.
giant|arms|colossusfist|Кулак колосса|Colossusfist|2.0|1.0|2.0|false|Один мах — и поля нет.
giant|legs|earthtreader|Земеход|Earthtreader|2.0|0.9|1.5|false|Тяжёлая поступь великанов.
giant|torso|atlasbulk|Атлантело|Atlasbulk|2.0|1.0|1.5|false|Плечи, держащие свод мира.
phantom|head|dreamhaunt|Сновидец|Dreamhaunt|1.0|1.2|1.0|false|Прилетает к тем, кто не спит.
phantom|arms|membraneclutch|Перепонкохват|Membraneclutch|1.0|1.0|1.0|false|Обвивает пергаментом кожи.
phantom|legs|hoverling|Левитант|Hoverling|1.0|1.3|1.0|false|Едва касается земли.
phantom|torso|lochloma|Лохлома|Lochloma|1.0|1.0|1.0|false|Плащ из обрывков крыльев.
zombie_villager|head|plaguelord|Чумной лорд|Plaguelord|1.5|1.0|1.5|false|Носитель мора среди живых.
zombie_villager|arms|plagueclasp|Чумозахват|Plagueclasp|1.0|1.0|1.0|false|Пожатие руки с мором.
zombie_villager|legs|plaguewalker|Чумоход|Plaguewalker|1.0|1.1|1.0|false|Где пройдёт — трава не растёт.
zombie_villager|torso|plaguecoat|Чумеплащ|Plaguecoat|1.0|1.0|1.0|false|Подол, пропахший чумой.
silverfish|head|silvermote|Сребропыль|Silvermote|1.0|1.2|1.0|false|Шуршит в стенах гробниц.
silverfish|arms|silverfingers|Серебропальцы|Silverfingers|1.0|1.0|1.0|false|Тонкие, как проволока.
silverfish|legs|wallcrawler|Стенолаз|Wallcrawler|1.0|1.4|1.0|false|Ползёт туда, где нет пола.
silverfish|torso|bristleback|Щетиноспин|Bristleback|1.0|1.0|1.0|false|Спина, дыбящаяся от света.
endermite|head|voidling|Пустотник|Voidling|1.0|1.2|1.0|false|Рождён из трещины между мирами.
endermite|arms|voidwrithing|Пустотокрут|Voidwrithing|1.0|1.0|1.0|false|Извивается без костей.
endermite|legs|crackskitter|Щелевик|Crackskitter|1.0|1.3|1.0|false|Шмыгает по трещинам пространства.
endermite|torso|chitinbelly|Хитинобок|Chitinbelly|1.0|1.0|1.0|false|Брюшко, звенящее, как стекло.
vex|head|tormented|Мучник|Tormented|1.0|1.3|1.0|false|Душа, не нашедшая покоя.
vex|arms|razorwing|Бритвокрыл|Razorwing|1.0|1.0|1.5|false|Крылья режут воздух.
vex|legs|flitstep|Мельтоток|Flitstep|1.0|1.4|1.0|false|Мелькает, не касаясь опоры.
vex|torso|gauzewrap|Марлевик|Gauzewrap|1.0|1.0|1.0|false|Пелена, ставшая плотью.
evoker|head|hexbinder|Плетун|Hexbinder|1.0|1.0|1.0|false|Завязывает судьбы в узлы.
evoker|arms|fangsummoner|Клыкорождающий|Fangsummoner|1.0|1.0|1.0|false|Вызывает зубы из земли.
evoker|legs|ritualist|Ритуалист|Ritualist|1.0|1.1|1.0|false|Вышагивает круги заклинаний.
evoker|torso|robebody|Мантиятело|Robebody|1.0|1.0|1.0|false|Мантия, что носит сама себя.
vindicator|head|cleaver|Тесак|Cleaver|1.0|1.0|2.0|false|Один удар — и имени нет.
vindicator|arms|butcherarm|Мясорук|Butcherarm|1.0|1.0|2.0|false|Рубит топором наотмашь.
vindicator|legs|axefoot|Секироног|Axefoot|1.0|1.2|1.0|false|Подходит вплотную быстро.
vindicator|torso|axeback|Топотоспин|Axeback|1.0|1.0|1.0|false|Спина, натёртая рукоятью.
illusioner|head|mirage|Мираж|Mirage|1.0|1.1|1.0|false|Обман зрячих и мёртвых.
illusioner|arms|miragehands|Миражоруки|Miragehands|1.0|1.0|1.0|false|Руки-обманки.
illusioner|legs|fakewalk|Ходообман|Fakewalk|1.0|1.0|1.0|false|Идёт, но следов не видно.
illusioner|torso|mirrorcoat|Зеркалка|Mirrorcoat|1.0|1.0|1.0|false|Кафтан, отражающий лишних.
pillager|head|marauder|Мародёр|Marauder|1.0|1.0|1.0|false|Грабит даже могилы.
pillager|arms|crossbowarm|Арбалторук|Crossbowarm|1.0|1.0|1.0|false|Рука-станок.
pillager|legs|raidstepper|Рейдер|Raidstepper|1.0|1.1|1.0|false|Шаги набега на деревню.
pillager|torso|captainside|Капитанбок|Captainside|1.0|1.0|1.0|false|Наградной кафтан рейдера.
ravager|head|behemoth|Левиафан|Behemoth|2.0|1.0|2.0|false|Хребтолом, идущий сквозь строй.
ravager|arms|lobberfist|Таранорука|Lobberfist|2.0|1.0|2.0|false|Сносит стену с разбега.
ravager|legs|siegebreaker|Стенобой|Siegebreaker|2.0|1.0|1.5|false|Ломит ворота одним весом.
ravager|torso|ramsided|Таранобок|Ramsided|2.0|1.0|1.0|false|Грудь, что идёт сквозь частокол.
warden|head|doomcaller|Зовущий рок|Doomcaller|2.0|1.0|2.0|false|Слышит биение сердец из-за стены.
warden|arms|sonicmaul|Звукобой|Sonicmaul|2.0|1.0|2.0|false|Бьёт звуком.
warden|legs|deepstrider|Глубиноход|Deepstrider|2.0|1.0|1.5|false|Идёт сквозь скалу.
warden|torso|sculkbod|Скалкобрюх|Sculkbod|2.0|1.0|1.0|false|Тело, проросшее скалком.
breeze|head|galewight|Ветреник|Galewight|1.0|1.3|1.0|false|Прыгучий сквозняк из ниоткуда.
breeze|arms|windlass|Ветротвод|Windlass|1.0|1.0|1.0|false|Крутит ветер, как лебёдку.
breeze|legs|galehopper|Сквозняк|Galehopper|1.0|1.5|1.0|false|Прыжки по потокам ветра.
breeze|torso|draftcore|Сквозносердие|Draftcore|1.0|1.0|1.0|false|В груди гуляет северный ветер.
slime|head|ichorling|Ихорник|Ichorling|1.0|1.1|1.0|false|Слизь, что помнит своего хозяина.
slime|arms|gooeygrip|Липкорук|Gooeygrip|1.0|1.0|1.0|false|Прилипнешь — не отклеишься.
slime|legs|bounceghast|Скакуша|Bounceghast|1.0|1.3|1.0|false|Подпрыгивает к горлу.
slime|torso|globbelly|Лопхеуз|Globbelly|1.0|1.0|1.0|false|Пузырь, что держит форму.
magma_cube|head|magmaling|Магмалинг|Magmaling|1.0|1.0|1.5|true|Искра бездны в луже смолы.
magma_cube|arms|tarclutch|Смологрыз|Tarclutch|1.0|1.0|1.5|true|Хватает смолой.
magma_cube|legs|cinderhops|Искроскок|Cinderhops|1.0|1.2|1.0|true|Капля лавы в человеческий рост.
magma_cube|torso|tarbod|Смоложоп|Tarbod|1.0|1.0|1.0|true|Смоляной бок, липкий и жаркий.
ghast|head|skyreaver|Небесный жилец|Skyreaver|1.5|1.0|1.5|true|Плачет огнём с низких сводов.
ghast|arms|tentaclewhip|Щупалка-хлыст|Tentaclewhip|1.0|1.0|1.5|true|Хлещет девятью хлыстами.
ghast|legs|cloudtreader|Облакомер|Cloudtreader|1.0|1.2|1.0|true|Ступает по облакам пепла.
ghast|torso|membranous|Перепончатый|Membranous|1.5|1.0|1.0|true|Белое брюхо, парящее под сводом.
shulker|head|boxlich|Лич-ларец|Boxlich|1.5|1.0|1.0|false|Сундук, который кусается первым.
shulker|arms|levitationclasp|Левитозахват|Levitationclasp|1.0|1.0|1.0|false|Поднимает в воздух.
shulker|legs|chestcrawler|Сундукополз|Chestcrawler|1.0|0.9|1.0|false|Волочит панцирь по ступеням.
shulker|torso|endershell|Эндощит|Endershell|1.5|1.0|1.0|false|Коробка из эндер-дерева.
guardian|head|pricklefin|Колючепёр|Pricklefin|1.5|1.0|1.0|false|Лучевик затонших храмов.
guardian|arms|laserpincher|Лучехват|Laserpincher|1.0|1.0|1.0|false|Заряжается и бьёт.
guardian|legs|reefwalker|Рифоход|Reefwalker|1.0|1.0|1.0|false|Идёт по дну мёртвого рифа.
guardian|torso|prismabulk|Призмобрюх|Prismabulk|1.5|1.0|1.0|false|Тело из морского стекла.
elder_guardian|head|deepbishop|Глубинный архиерей|Deepbishop|2.0|0.9|1.5|false|Благословляет трепетом.
elder_guardian|arms|mininggrip|Киркохват|Mininggrip|1.5|1.0|1.0|false|Ослабляет броню взглядом.
elder_guardian|legs|abysspad|Бездонная лапа|Abysspad|2.0|0.8|1.0|false|Тянет на дно одним взглядом.
elder_guardian|torso|ancientside|Древнебок|Ancientside|2.0|1.0|1.0|false|Бока, покрытые наростами веков.
'''


def load_rows():
    rows = []
    for line in HYBRIDS_RAW.strip().splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        c = line.split('|')
        assert len(c) == 10, 'bad cols (%d): %s' % (len(c), line[:60])
        donor, part, hid, ru, en, hp, sp, dm, fi, desc = c
        assert part in PARTS, 'bad part: %s' % part
        assert donor in DONOR_RU, 'unknown donor: %s' % donor
        rows.append(dict(donor='minecraft:' + donor, dshort=donor, part=part, id=hid,
                         ru=ru, en=en, hp=float(hp), sp=float(sp), dm=float(dm),
                         fi=(fi == 'true'), desc=desc))
    ids = [r['id'] for r in rows]
    dup = sorted(set(i for i in ids if ids.count(i) > 1))
    assert not dup, 'duplicate hybrid ids: %s' % dup
    pairs = [(r['donor'], r['part']) for r in rows]
    dp = sorted(set(p for p in pairs if pairs.count(p) > 1))
    assert not dp, 'duplicate (donor,part) pairs: %s' % dp
    return rows
