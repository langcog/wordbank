from django.db import models
from base import BaseTable


class English_WS(BaseTable):
    baa_baa_choices = [(u'produces', u'produces')]
    item_baa_baa = models.CharField(max_length=20, choices=baa_baa_choices, null=True)
    choo_choo_choices = [(u'produces', u'produces')]
    item_choo_choo = models.CharField(max_length=20, choices=choo_choo_choices, null=True)
    cockadoodledoo_choices = [(u'produces', u'produces')]
    item_cockadoodledoo = models.CharField(max_length=20, choices=cockadoodledoo_choices, null=True)
    grrr_choices = [(u'produces', u'produces')]
    item_grrr = models.CharField(max_length=20, choices=grrr_choices, null=True)
    meow_choices = [(u'produces', u'produces')]
    item_meow = models.CharField(max_length=20, choices=meow_choices, null=True)
    moo_choices = [(u'produces', u'produces')]
    item_moo = models.CharField(max_length=20, choices=moo_choices, null=True)
    ouch_choices = [(u'produces', u'produces')]
    item_ouch = models.CharField(max_length=20, choices=ouch_choices, null=True)
    quack_quack_choices = [(u'produces', u'produces')]
    item_quack_quack = models.CharField(max_length=20, choices=quack_quack_choices, null=True)
    uh_oh_choices = [(u'produces', u'produces')]
    item_uh_oh = models.CharField(max_length=20, choices=uh_oh_choices, null=True)
    vroom_choices = [(u'produces', u'produces')]
    item_vroom = models.CharField(max_length=20, choices=vroom_choices, null=True)
    woof_woof_choices = [(u'produces', u'produces')]
    item_woof_woof = models.CharField(max_length=20, choices=woof_woof_choices, null=True)
    yum_yum_choices = [(u'produces', u'produces')]
    item_yum_yum = models.CharField(max_length=20, choices=yum_yum_choices, null=True)
    alligator_choices = [(u'produces', u'produces')]
    item_alligator = models.CharField(max_length=20, choices=alligator_choices, null=True)
    animal_choices = [(u'produces', u'produces')]
    item_animal = models.CharField(max_length=20, choices=animal_choices, null=True)
    ant_choices = [(u'produces', u'produces')]
    item_ant = models.CharField(max_length=20, choices=ant_choices, null=True)
    bear_choices = [(u'produces', u'produces')]
    item_bear = models.CharField(max_length=20, choices=bear_choices, null=True)
    bee_choices = [(u'produces', u'produces')]
    item_bee = models.CharField(max_length=20, choices=bee_choices, null=True)
    bird_choices = [(u'produces', u'produces')]
    item_bird = models.CharField(max_length=20, choices=bird_choices, null=True)
    bug_choices = [(u'produces', u'produces')]
    item_bug = models.CharField(max_length=20, choices=bug_choices, null=True)
    bunny_choices = [(u'produces', u'produces')]
    item_bunny = models.CharField(max_length=20, choices=bunny_choices, null=True)
    butterfly_choices = [(u'produces', u'produces')]
    item_butterfly = models.CharField(max_length=20, choices=butterfly_choices, null=True)
    cat_choices = [(u'produces', u'produces')]
    item_cat = models.CharField(max_length=20, choices=cat_choices, null=True)
    chicken_animal_choices = [(u'produces', u'produces')]
    item_chicken_animal = models.CharField(max_length=20, choices=chicken_animal_choices, null=True)
    cow_choices = [(u'produces', u'produces')]
    item_cow = models.CharField(max_length=20, choices=cow_choices, null=True)
    deer_choices = [(u'produces', u'produces')]
    item_deer = models.CharField(max_length=20, choices=deer_choices, null=True)
    dog_choices = [(u'produces', u'produces')]
    item_dog = models.CharField(max_length=20, choices=dog_choices, null=True)
    donkey_choices = [(u'produces', u'produces')]
    item_donkey = models.CharField(max_length=20, choices=donkey_choices, null=True)
    duck_choices = [(u'produces', u'produces')]
    item_duck = models.CharField(max_length=20, choices=duck_choices, null=True)
    elephant_choices = [(u'produces', u'produces')]
    item_elephant = models.CharField(max_length=20, choices=elephant_choices, null=True)
    fish_animal_choices = [(u'produces', u'produces')]
    item_fish_animal = models.CharField(max_length=20, choices=fish_animal_choices, null=True)
    frog_choices = [(u'produces', u'produces')]
    item_frog = models.CharField(max_length=20, choices=frog_choices, null=True)
    giraffe_choices = [(u'produces', u'produces')]
    item_giraffe = models.CharField(max_length=20, choices=giraffe_choices, null=True)
    goose_choices = [(u'produces', u'produces')]
    item_goose = models.CharField(max_length=20, choices=goose_choices, null=True)
    hen_choices = [(u'produces', u'produces')]
    item_hen = models.CharField(max_length=20, choices=hen_choices, null=True)
    horse_choices = [(u'produces', u'produces')]
    item_horse = models.CharField(max_length=20, choices=horse_choices, null=True)
    kitty_choices = [(u'produces', u'produces')]
    item_kitty = models.CharField(max_length=20, choices=kitty_choices, null=True)
    lamb_choices = [(u'produces', u'produces')]
    item_lamb = models.CharField(max_length=20, choices=lamb_choices, null=True)
    lion_choices = [(u'produces', u'produces')]
    item_lion = models.CharField(max_length=20, choices=lion_choices, null=True)
    monkey_choices = [(u'produces', u'produces')]
    item_monkey = models.CharField(max_length=20, choices=monkey_choices, null=True)
    moose_choices = [(u'produces', u'produces')]
    item_moose = models.CharField(max_length=20, choices=moose_choices, null=True)
    mouse_choices = [(u'produces', u'produces')]
    item_mouse = models.CharField(max_length=20, choices=mouse_choices, null=True)
    owl_choices = [(u'produces', u'produces')]
    item_owl = models.CharField(max_length=20, choices=owl_choices, null=True)
    penguin_choices = [(u'produces', u'produces')]
    item_penguin = models.CharField(max_length=20, choices=penguin_choices, null=True)
    pig_choices = [(u'produces', u'produces')]
    item_pig = models.CharField(max_length=20, choices=pig_choices, null=True)
    pony_choices = [(u'produces', u'produces')]
    item_pony = models.CharField(max_length=20, choices=pony_choices, null=True)
    puppy_choices = [(u'produces', u'produces')]
    item_puppy = models.CharField(max_length=20, choices=puppy_choices, null=True)
    rooster_choices = [(u'produces', u'produces')]
    item_rooster = models.CharField(max_length=20, choices=rooster_choices, null=True)
    sheep_choices = [(u'produces', u'produces')]
    item_sheep = models.CharField(max_length=20, choices=sheep_choices, null=True)
    squirrel_choices = [(u'produces', u'produces')]
    item_squirrel = models.CharField(max_length=20, choices=squirrel_choices, null=True)
    teddybear_choices = [(u'produces', u'produces')]
    item_teddybear = models.CharField(max_length=20, choices=teddybear_choices, null=True)
    tiger_choices = [(u'produces', u'produces')]
    item_tiger = models.CharField(max_length=20, choices=tiger_choices, null=True)
    turkey_choices = [(u'produces', u'produces')]
    item_turkey = models.CharField(max_length=20, choices=turkey_choices, null=True)
    turtle_choices = [(u'produces', u'produces')]
    item_turtle = models.CharField(max_length=20, choices=turtle_choices, null=True)
    wolf_choices = [(u'produces', u'produces')]
    item_wolf = models.CharField(max_length=20, choices=wolf_choices, null=True)
    zebra_choices = [(u'produces', u'produces')]
    item_zebra = models.CharField(max_length=20, choices=zebra_choices, null=True)
    airplane_choices = [(u'produces', u'produces')]
    item_airplane = models.CharField(max_length=20, choices=airplane_choices, null=True)
    bicycle_choices = [(u'produces', u'produces')]
    item_bicycle = models.CharField(max_length=20, choices=bicycle_choices, null=True)
    boat_choices = [(u'produces', u'produces')]
    item_boat = models.CharField(max_length=20, choices=boat_choices, null=True)
    bus_choices = [(u'produces', u'produces')]
    item_bus = models.CharField(max_length=20, choices=bus_choices, null=True)
    car_choices = [(u'produces', u'produces')]
    item_car = models.CharField(max_length=20, choices=car_choices, null=True)
    firetruck_choices = [(u'produces', u'produces')]
    item_firetruck = models.CharField(max_length=20, choices=firetruck_choices, null=True)
    helicopter_choices = [(u'produces', u'produces')]
    item_helicopter = models.CharField(max_length=20, choices=helicopter_choices, null=True)
    motorcycle_choices = [(u'produces', u'produces')]
    item_motorcycle = models.CharField(max_length=20, choices=motorcycle_choices, null=True)
    sled_choices = [(u'produces', u'produces')]
    item_sled = models.CharField(max_length=20, choices=sled_choices, null=True)
    stroller_choices = [(u'produces', u'produces')]
    item_stroller = models.CharField(max_length=20, choices=stroller_choices, null=True)
    tractor_choices = [(u'produces', u'produces')]
    item_tractor = models.CharField(max_length=20, choices=tractor_choices, null=True)
    train_choices = [(u'produces', u'produces')]
    item_train = models.CharField(max_length=20, choices=train_choices, null=True)
    tricycle_choices = [(u'produces', u'produces')]
    item_tricycle = models.CharField(max_length=20, choices=tricycle_choices, null=True)
    truck_choices = [(u'produces', u'produces')]
    item_truck = models.CharField(max_length=20, choices=truck_choices, null=True)
    ball_choices = [(u'produces', u'produces')]
    item_ball = models.CharField(max_length=20, choices=ball_choices, null=True)
    balloon_choices = [(u'produces', u'produces')]
    item_balloon = models.CharField(max_length=20, choices=balloon_choices, null=True)
    bat_choices = [(u'produces', u'produces')]
    item_bat = models.CharField(max_length=20, choices=bat_choices, null=True)
    block_choices = [(u'produces', u'produces')]
    item_block = models.CharField(max_length=20, choices=block_choices, null=True)
    book_choices = [(u'produces', u'produces')]
    item_book = models.CharField(max_length=20, choices=book_choices, null=True)
    bubbles_choices = [(u'produces', u'produces')]
    item_bubbles = models.CharField(max_length=20, choices=bubbles_choices, null=True)
    chalk_choices = [(u'produces', u'produces')]
    item_chalk = models.CharField(max_length=20, choices=chalk_choices, null=True)
    crayon_choices = [(u'produces', u'produces')]
    item_crayon = models.CharField(max_length=20, choices=crayon_choices, null=True)
    doll_choices = [(u'produces', u'produces')]
    item_doll = models.CharField(max_length=20, choices=doll_choices, null=True)
    game_choices = [(u'produces', u'produces')]
    item_game = models.CharField(max_length=20, choices=game_choices, null=True)
    glue_choices = [(u'produces', u'produces')]
    item_glue = models.CharField(max_length=20, choices=glue_choices, null=True)
    pen_choices = [(u'produces', u'produces')]
    item_pen = models.CharField(max_length=20, choices=pen_choices, null=True)
    pencil_choices = [(u'produces', u'produces')]
    item_pencil = models.CharField(max_length=20, choices=pencil_choices, null=True)
    play_dough_choices = [(u'produces', u'produces')]
    item_play_dough = models.CharField(max_length=20, choices=play_dough_choices, null=True)
    present_choices = [(u'produces', u'produces')]
    item_present = models.CharField(max_length=20, choices=present_choices, null=True)
    puzzle_choices = [(u'produces', u'produces')]
    item_puzzle = models.CharField(max_length=20, choices=puzzle_choices, null=True)
    story_choices = [(u'produces', u'produces')]
    item_story = models.CharField(max_length=20, choices=story_choices, null=True)
    toy_choices = [(u'produces', u'produces')]
    item_toy = models.CharField(max_length=20, choices=toy_choices, null=True)
    apple_choices = [(u'produces', u'produces')]
    item_apple = models.CharField(max_length=20, choices=apple_choices, null=True)
    applesauce_choices = [(u'produces', u'produces')]
    item_applesauce = models.CharField(max_length=20, choices=applesauce_choices, null=True)
    banana_choices = [(u'produces', u'produces')]
    item_banana = models.CharField(max_length=20, choices=banana_choices, null=True)
    beans_choices = [(u'produces', u'produces')]
    item_beans = models.CharField(max_length=20, choices=beans_choices, null=True)
    bread_choices = [(u'produces', u'produces')]
    item_bread = models.CharField(max_length=20, choices=bread_choices, null=True)
    butter_choices = [(u'produces', u'produces')]
    item_butter = models.CharField(max_length=20, choices=butter_choices, null=True)
    cake_choices = [(u'produces', u'produces')]
    item_cake = models.CharField(max_length=20, choices=cake_choices, null=True)
    candy_choices = [(u'produces', u'produces')]
    item_candy = models.CharField(max_length=20, choices=candy_choices, null=True)
    carrots_choices = [(u'produces', u'produces')]
    item_carrots = models.CharField(max_length=20, choices=carrots_choices, null=True)
    cereal_choices = [(u'produces', u'produces')]
    item_cereal = models.CharField(max_length=20, choices=cereal_choices, null=True)
    cheerios_choices = [(u'produces', u'produces')]
    item_cheerios = models.CharField(max_length=20, choices=cheerios_choices, null=True)
    cheese_choices = [(u'produces', u'produces')]
    item_cheese = models.CharField(max_length=20, choices=cheese_choices, null=True)
    chicken_food_choices = [(u'produces', u'produces')]
    item_chicken_food = models.CharField(max_length=20, choices=chicken_food_choices, null=True)
    chocolate_choices = [(u'produces', u'produces')]
    item_chocolate = models.CharField(max_length=20, choices=chocolate_choices, null=True)
    coffee_choices = [(u'produces', u'produces')]
    item_coffee = models.CharField(max_length=20, choices=coffee_choices, null=True)
    coke_choices = [(u'produces', u'produces')]
    item_coke = models.CharField(max_length=20, choices=coke_choices, null=True)
    cookie_choices = [(u'produces', u'produces')]
    item_cookie = models.CharField(max_length=20, choices=cookie_choices, null=True)
    corn_choices = [(u'produces', u'produces')]
    item_corn = models.CharField(max_length=20, choices=corn_choices, null=True)
    cracker_choices = [(u'produces', u'produces')]
    item_cracker = models.CharField(max_length=20, choices=cracker_choices, null=True)
    donut_choices = [(u'produces', u'produces')]
    item_donut = models.CharField(max_length=20, choices=donut_choices, null=True)
    drink_beverage_choices = [(u'produces', u'produces')]
    item_drink_beverage = models.CharField(max_length=20, choices=drink_beverage_choices, null=True)
    egg_choices = [(u'produces', u'produces')]
    item_egg = models.CharField(max_length=20, choices=egg_choices, null=True)
    fish_food_choices = [(u'produces', u'produces')]
    item_fish_food = models.CharField(max_length=20, choices=fish_food_choices, null=True)
    food_choices = [(u'produces', u'produces')]
    item_food = models.CharField(max_length=20, choices=food_choices, null=True)
    french_fries_choices = [(u'produces', u'produces')]
    item_french_fries = models.CharField(max_length=20, choices=french_fries_choices, null=True)
    grapes_choices = [(u'produces', u'produces')]
    item_grapes = models.CharField(max_length=20, choices=grapes_choices, null=True)
    green_beans_choices = [(u'produces', u'produces')]
    item_green_beans = models.CharField(max_length=20, choices=green_beans_choices, null=True)
    gum_choices = [(u'produces', u'produces')]
    item_gum = models.CharField(max_length=20, choices=gum_choices, null=True)
    hamburger_choices = [(u'produces', u'produces')]
    item_hamburger = models.CharField(max_length=20, choices=hamburger_choices, null=True)
    ice_choices = [(u'produces', u'produces')]
    item_ice = models.CharField(max_length=20, choices=ice_choices, null=True)
    ice_cream_choices = [(u'produces', u'produces')]
    item_ice_cream = models.CharField(max_length=20, choices=ice_cream_choices, null=True)
    jello_choices = [(u'produces', u'produces')]
    item_jello = models.CharField(max_length=20, choices=jello_choices, null=True)
    jelly_choices = [(u'produces', u'produces')]
    item_jelly = models.CharField(max_length=20, choices=jelly_choices, null=True)
    juice_choices = [(u'produces', u'produces')]
    item_juice = models.CharField(max_length=20, choices=juice_choices, null=True)
    lollipop_choices = [(u'produces', u'produces')]
    item_lollipop = models.CharField(max_length=20, choices=lollipop_choices, null=True)
    meat_choices = [(u'produces', u'produces')]
    item_meat = models.CharField(max_length=20, choices=meat_choices, null=True)
    melon_choices = [(u'produces', u'produces')]
    item_melon = models.CharField(max_length=20, choices=melon_choices, null=True)
    milk_choices = [(u'produces', u'produces')]
    item_milk = models.CharField(max_length=20, choices=milk_choices, null=True)
    muffin_choices = [(u'produces', u'produces')]
    item_muffin = models.CharField(max_length=20, choices=muffin_choices, null=True)
    noodles_choices = [(u'produces', u'produces')]
    item_noodles = models.CharField(max_length=20, choices=noodles_choices, null=True)
    nuts_choices = [(u'produces', u'produces')]
    item_nuts = models.CharField(max_length=20, choices=nuts_choices, null=True)
    orange_food_choices = [(u'produces', u'produces')]
    item_orange_food = models.CharField(max_length=20, choices=orange_food_choices, null=True)
    pancake_choices = [(u'produces', u'produces')]
    item_pancake = models.CharField(max_length=20, choices=pancake_choices, null=True)
    peas_choices = [(u'produces', u'produces')]
    item_peas = models.CharField(max_length=20, choices=peas_choices, null=True)
    peanut_butter_choices = [(u'produces', u'produces')]
    item_peanut_butter = models.CharField(max_length=20, choices=peanut_butter_choices, null=True)
    pickle_choices = [(u'produces', u'produces')]
    item_pickle = models.CharField(max_length=20, choices=pickle_choices, null=True)
    pizza_choices = [(u'produces', u'produces')]
    item_pizza = models.CharField(max_length=20, choices=pizza_choices, null=True)
    popcorn_choices = [(u'produces', u'produces')]
    item_popcorn = models.CharField(max_length=20, choices=popcorn_choices, null=True)
    popsicle_choices = [(u'produces', u'produces')]
    item_popsicle = models.CharField(max_length=20, choices=popsicle_choices, null=True)
    potato_chip_choices = [(u'produces', u'produces')]
    item_potato_chip = models.CharField(max_length=20, choices=potato_chip_choices, null=True)
    potato_choices = [(u'produces', u'produces')]
    item_potato = models.CharField(max_length=20, choices=potato_choices, null=True)
    pretzel_choices = [(u'produces', u'produces')]
    item_pretzel = models.CharField(max_length=20, choices=pretzel_choices, null=True)
    pudding_choices = [(u'produces', u'produces')]
    item_pudding = models.CharField(max_length=20, choices=pudding_choices, null=True)
    pumpkin_choices = [(u'produces', u'produces')]
    item_pumpkin = models.CharField(max_length=20, choices=pumpkin_choices, null=True)
    raisin_choices = [(u'produces', u'produces')]
    item_raisin = models.CharField(max_length=20, choices=raisin_choices, null=True)
    salt_choices = [(u'produces', u'produces')]
    item_salt = models.CharField(max_length=20, choices=salt_choices, null=True)
    sandwich_choices = [(u'produces', u'produces')]
    item_sandwich = models.CharField(max_length=20, choices=sandwich_choices, null=True)
    sauce_choices = [(u'produces', u'produces')]
    item_sauce = models.CharField(max_length=20, choices=sauce_choices, null=True)
    soda_choices = [(u'produces', u'produces')]
    item_soda = models.CharField(max_length=20, choices=soda_choices, null=True)
    soup_choices = [(u'produces', u'produces')]
    item_soup = models.CharField(max_length=20, choices=soup_choices, null=True)
    spaghetti_choices = [(u'produces', u'produces')]
    item_spaghetti = models.CharField(max_length=20, choices=spaghetti_choices, null=True)
    strawberry_choices = [(u'produces', u'produces')]
    item_strawberry = models.CharField(max_length=20, choices=strawberry_choices, null=True)
    toast_choices = [(u'produces', u'produces')]
    item_toast = models.CharField(max_length=20, choices=toast_choices, null=True)
    tuna_choices = [(u'produces', u'produces')]
    item_tuna = models.CharField(max_length=20, choices=tuna_choices, null=True)
    vanilla_choices = [(u'produces', u'produces')]
    item_vanilla = models.CharField(max_length=20, choices=vanilla_choices, null=True)
    vitamins_choices = [(u'produces', u'produces')]
    item_vitamins = models.CharField(max_length=20, choices=vitamins_choices, null=True)
    water_beverage_choices = [(u'produces', u'produces')]
    item_water_beverage = models.CharField(max_length=20, choices=water_beverage_choices, null=True)
    yogurt_choices = [(u'produces', u'produces')]
    item_yogurt = models.CharField(max_length=20, choices=yogurt_choices, null=True)
    beads_choices = [(u'produces', u'produces')]
    item_beads = models.CharField(max_length=20, choices=beads_choices, null=True)
    belt_choices = [(u'produces', u'produces')]
    item_belt = models.CharField(max_length=20, choices=belt_choices, null=True)
    bib_choices = [(u'produces', u'produces')]
    item_bib = models.CharField(max_length=20, choices=bib_choices, null=True)
    boots_choices = [(u'produces', u'produces')]
    item_boots = models.CharField(max_length=20, choices=boots_choices, null=True)
    button_choices = [(u'produces', u'produces')]
    item_button = models.CharField(max_length=20, choices=button_choices, null=True)
    coat_choices = [(u'produces', u'produces')]
    item_coat = models.CharField(max_length=20, choices=coat_choices, null=True)
    diaper_choices = [(u'produces', u'produces')]
    item_diaper = models.CharField(max_length=20, choices=diaper_choices, null=True)
    dress_choices = [(u'produces', u'produces')]
    item_dress = models.CharField(max_length=20, choices=dress_choices, null=True)
    gloves_choices = [(u'produces', u'produces')]
    item_gloves = models.CharField(max_length=20, choices=gloves_choices, null=True)
    hat_choices = [(u'produces', u'produces')]
    item_hat = models.CharField(max_length=20, choices=hat_choices, null=True)
    jacket_choices = [(u'produces', u'produces')]
    item_jacket = models.CharField(max_length=20, choices=jacket_choices, null=True)
    jeans_choices = [(u'produces', u'produces')]
    item_jeans = models.CharField(max_length=20, choices=jeans_choices, null=True)
    mittens_choices = [(u'produces', u'produces')]
    item_mittens = models.CharField(max_length=20, choices=mittens_choices, null=True)
    necklace_choices = [(u'produces', u'produces')]
    item_necklace = models.CharField(max_length=20, choices=necklace_choices, null=True)
    pajamas_choices = [(u'produces', u'produces')]
    item_pajamas = models.CharField(max_length=20, choices=pajamas_choices, null=True)
    pants_choices = [(u'produces', u'produces')]
    item_pants = models.CharField(max_length=20, choices=pants_choices, null=True)
    scarf_choices = [(u'produces', u'produces')]
    item_scarf = models.CharField(max_length=20, choices=scarf_choices, null=True)
    shirt_choices = [(u'produces', u'produces')]
    item_shirt = models.CharField(max_length=20, choices=shirt_choices, null=True)
    shoe_choices = [(u'produces', u'produces')]
    item_shoe = models.CharField(max_length=20, choices=shoe_choices, null=True)
    shorts_choices = [(u'produces', u'produces')]
    item_shorts = models.CharField(max_length=20, choices=shorts_choices, null=True)
    slipper_choices = [(u'produces', u'produces')]
    item_slipper = models.CharField(max_length=20, choices=slipper_choices, null=True)
    sneaker_choices = [(u'produces', u'produces')]
    item_sneaker = models.CharField(max_length=20, choices=sneaker_choices, null=True)
    snowsuit_choices = [(u'produces', u'produces')]
    item_snowsuit = models.CharField(max_length=20, choices=snowsuit_choices, null=True)
    sock_choices = [(u'produces', u'produces')]
    item_sock = models.CharField(max_length=20, choices=sock_choices, null=True)
    sweater_choices = [(u'produces', u'produces')]
    item_sweater = models.CharField(max_length=20, choices=sweater_choices, null=True)
    tights_choices = [(u'produces', u'produces')]
    item_tights = models.CharField(max_length=20, choices=tights_choices, null=True)
    underpants_choices = [(u'produces', u'produces')]
    item_underpants = models.CharField(max_length=20, choices=underpants_choices, null=True)
    zipper_choices = [(u'produces', u'produces')]
    item_zipper = models.CharField(max_length=20, choices=zipper_choices, null=True)
    ankle_choices = [(u'produces', u'produces')]
    item_ankle = models.CharField(max_length=20, choices=ankle_choices, null=True)
    arm_choices = [(u'produces', u'produces')]
    item_arm = models.CharField(max_length=20, choices=arm_choices, null=True)
    belly_button_choices = [(u'produces', u'produces')]
    item_belly_button = models.CharField(max_length=20, choices=belly_button_choices, null=True)
    buttocks_choices = [(u'produces', u'produces')]
    item_buttocks = models.CharField(max_length=20, choices=buttocks_choices, null=True)
    cheek_choices = [(u'produces', u'produces')]
    item_cheek = models.CharField(max_length=20, choices=cheek_choices, null=True)
    chin_choices = [(u'produces', u'produces')]
    item_chin = models.CharField(max_length=20, choices=chin_choices, null=True)
    ear_choices = [(u'produces', u'produces')]
    item_ear = models.CharField(max_length=20, choices=ear_choices, null=True)
    eye_choices = [(u'produces', u'produces')]
    item_eye = models.CharField(max_length=20, choices=eye_choices, null=True)
    face_choices = [(u'produces', u'produces')]
    item_face = models.CharField(max_length=20, choices=face_choices, null=True)
    finger_choices = [(u'produces', u'produces')]
    item_finger = models.CharField(max_length=20, choices=finger_choices, null=True)
    foot_choices = [(u'produces', u'produces')]
    item_foot = models.CharField(max_length=20, choices=foot_choices, null=True)
    hair_choices = [(u'produces', u'produces')]
    item_hair = models.CharField(max_length=20, choices=hair_choices, null=True)
    hand_choices = [(u'produces', u'produces')]
    item_hand = models.CharField(max_length=20, choices=hand_choices, null=True)
    head_choices = [(u'produces', u'produces')]
    item_head = models.CharField(max_length=20, choices=head_choices, null=True)
    knee_choices = [(u'produces', u'produces')]
    item_knee = models.CharField(max_length=20, choices=knee_choices, null=True)
    leg_choices = [(u'produces', u'produces')]
    item_leg = models.CharField(max_length=20, choices=leg_choices, null=True)
    lips_choices = [(u'produces', u'produces')]
    item_lips = models.CharField(max_length=20, choices=lips_choices, null=True)
    mouth_choices = [(u'produces', u'produces')]
    item_mouth = models.CharField(max_length=20, choices=mouth_choices, null=True)
    nose_choices = [(u'produces', u'produces')]
    item_nose = models.CharField(max_length=20, choices=nose_choices, null=True)
    owie_choices = [(u'produces', u'produces')]
    item_owie = models.CharField(max_length=20, choices=owie_choices, null=True)
    penis_choices = [(u'produces', u'produces')]
    item_penis = models.CharField(max_length=20, choices=penis_choices, null=True)
    shoulder_choices = [(u'produces', u'produces')]
    item_shoulder = models.CharField(max_length=20, choices=shoulder_choices, null=True)
    toe_choices = [(u'produces', u'produces')]
    item_toe = models.CharField(max_length=20, choices=toe_choices, null=True)
    tongue_choices = [(u'produces', u'produces')]
    item_tongue = models.CharField(max_length=20, choices=tongue_choices, null=True)
    tooth_choices = [(u'produces', u'produces')]
    item_tooth = models.CharField(max_length=20, choices=tooth_choices, null=True)
    tummy_choices = [(u'produces', u'produces')]
    item_tummy = models.CharField(max_length=20, choices=tummy_choices, null=True)
    vagina_choices = [(u'produces', u'produces')]
    item_vagina = models.CharField(max_length=20, choices=vagina_choices, null=True)
    basket_choices = [(u'produces', u'produces')]
    item_basket = models.CharField(max_length=20, choices=basket_choices, null=True)
    blanket_choices = [(u'produces', u'produces')]
    item_blanket = models.CharField(max_length=20, choices=blanket_choices, null=True)
    bottle_choices = [(u'produces', u'produces')]
    item_bottle = models.CharField(max_length=20, choices=bottle_choices, null=True)
    bowl_choices = [(u'produces', u'produces')]
    item_bowl = models.CharField(max_length=20, choices=bowl_choices, null=True)
    box_choices = [(u'produces', u'produces')]
    item_box = models.CharField(max_length=20, choices=box_choices, null=True)
    broom_choices = [(u'produces', u'produces')]
    item_broom = models.CharField(max_length=20, choices=broom_choices, null=True)
    brush_choices = [(u'produces', u'produces')]
    item_brush = models.CharField(max_length=20, choices=brush_choices, null=True)
    bucket_choices = [(u'produces', u'produces')]
    item_bucket = models.CharField(max_length=20, choices=bucket_choices, null=True)
    camera_choices = [(u'produces', u'produces')]
    item_camera = models.CharField(max_length=20, choices=camera_choices, null=True)
    can_object_choices = [(u'produces', u'produces')]
    item_can_object = models.CharField(max_length=20, choices=can_object_choices, null=True)
    clock_choices = [(u'produces', u'produces')]
    item_clock = models.CharField(max_length=20, choices=clock_choices, null=True)
    comb_choices = [(u'produces', u'produces')]
    item_comb = models.CharField(max_length=20, choices=comb_choices, null=True)
    cup_choices = [(u'produces', u'produces')]
    item_cup = models.CharField(max_length=20, choices=cup_choices, null=True)
    dish_choices = [(u'produces', u'produces')]
    item_dish = models.CharField(max_length=20, choices=dish_choices, null=True)
    fork_choices = [(u'produces', u'produces')]
    item_fork = models.CharField(max_length=20, choices=fork_choices, null=True)
    garbage_choices = [(u'produces', u'produces')]
    item_garbage = models.CharField(max_length=20, choices=garbage_choices, null=True)
    glass_choices = [(u'produces', u'produces')]
    item_glass = models.CharField(max_length=20, choices=glass_choices, null=True)
    glasses_choices = [(u'produces', u'produces')]
    item_glasses = models.CharField(max_length=20, choices=glasses_choices, null=True)
    hammer_choices = [(u'produces', u'produces')]
    item_hammer = models.CharField(max_length=20, choices=hammer_choices, null=True)
    jar_choices = [(u'produces', u'produces')]
    item_jar = models.CharField(max_length=20, choices=jar_choices, null=True)
    keys_choices = [(u'produces', u'produces')]
    item_keys = models.CharField(max_length=20, choices=keys_choices, null=True)
    knife_choices = [(u'produces', u'produces')]
    item_knife = models.CharField(max_length=20, choices=knife_choices, null=True)
    lamp_choices = [(u'produces', u'produces')]
    item_lamp = models.CharField(max_length=20, choices=lamp_choices, null=True)
    light_choices = [(u'produces', u'produces')]
    item_light = models.CharField(max_length=20, choices=light_choices, null=True)
    medicine_choices = [(u'produces', u'produces')]
    item_medicine = models.CharField(max_length=20, choices=medicine_choices, null=True)
    money_choices = [(u'produces', u'produces')]
    item_money = models.CharField(max_length=20, choices=money_choices, null=True)
    mop_choices = [(u'produces', u'produces')]
    item_mop = models.CharField(max_length=20, choices=mop_choices, null=True)
    nail_choices = [(u'produces', u'produces')]
    item_nail = models.CharField(max_length=20, choices=nail_choices, null=True)
    napkin_choices = [(u'produces', u'produces')]
    item_napkin = models.CharField(max_length=20, choices=napkin_choices, null=True)
    paper_choices = [(u'produces', u'produces')]
    item_paper = models.CharField(max_length=20, choices=paper_choices, null=True)
    penny_choices = [(u'produces', u'produces')]
    item_penny = models.CharField(max_length=20, choices=penny_choices, null=True)
    picture_choices = [(u'produces', u'produces')]
    item_picture = models.CharField(max_length=20, choices=picture_choices, null=True)
    pillow_choices = [(u'produces', u'produces')]
    item_pillow = models.CharField(max_length=20, choices=pillow_choices, null=True)
    plant_choices = [(u'produces', u'produces')]
    item_plant = models.CharField(max_length=20, choices=plant_choices, null=True)
    plate_choices = [(u'produces', u'produces')]
    item_plate = models.CharField(max_length=20, choices=plate_choices, null=True)
    purse_choices = [(u'produces', u'produces')]
    item_purse = models.CharField(max_length=20, choices=purse_choices, null=True)
    radio_choices = [(u'produces', u'produces')]
    item_radio = models.CharField(max_length=20, choices=radio_choices, null=True)
    scissors_choices = [(u'produces', u'produces')]
    item_scissors = models.CharField(max_length=20, choices=scissors_choices, null=True)
    soap_choices = [(u'produces', u'produces')]
    item_soap = models.CharField(max_length=20, choices=soap_choices, null=True)
    spoon_choices = [(u'produces', u'produces')]
    item_spoon = models.CharField(max_length=20, choices=spoon_choices, null=True)
    tape_choices = [(u'produces', u'produces')]
    item_tape = models.CharField(max_length=20, choices=tape_choices, null=True)
    telephone_choices = [(u'produces', u'produces')]
    item_telephone = models.CharField(max_length=20, choices=telephone_choices, null=True)
    tissue_choices = [(u'produces', u'produces')]
    item_tissue = models.CharField(max_length=20, choices=tissue_choices, null=True)
    toothbrush_choices = [(u'produces', u'produces')]
    item_toothbrush = models.CharField(max_length=20, choices=toothbrush_choices, null=True)
    towel_choices = [(u'produces', u'produces')]
    item_towel = models.CharField(max_length=20, choices=towel_choices, null=True)
    trash_choices = [(u'produces', u'produces')]
    item_trash = models.CharField(max_length=20, choices=trash_choices, null=True)
    tray_choices = [(u'produces', u'produces')]
    item_tray = models.CharField(max_length=20, choices=tray_choices, null=True)
    vacuum_choices = [(u'produces', u'produces')]
    item_vacuum = models.CharField(max_length=20, choices=vacuum_choices, null=True)
    walker_choices = [(u'produces', u'produces')]
    item_walker = models.CharField(max_length=20, choices=walker_choices, null=True)
    watch_object_choices = [(u'produces', u'produces')]
    item_watch_object = models.CharField(max_length=20, choices=watch_object_choices, null=True)
    basement_choices = [(u'produces', u'produces')]
    item_basement = models.CharField(max_length=20, choices=basement_choices, null=True)
    bathroom_choices = [(u'produces', u'produces')]
    item_bathroom = models.CharField(max_length=20, choices=bathroom_choices, null=True)
    bathtub_choices = [(u'produces', u'produces')]
    item_bathtub = models.CharField(max_length=20, choices=bathtub_choices, null=True)
    bed_choices = [(u'produces', u'produces')]
    item_bed = models.CharField(max_length=20, choices=bed_choices, null=True)
    bedroom_choices = [(u'produces', u'produces')]
    item_bedroom = models.CharField(max_length=20, choices=bedroom_choices, null=True)
    bench_choices = [(u'produces', u'produces')]
    item_bench = models.CharField(max_length=20, choices=bench_choices, null=True)
    chair_choices = [(u'produces', u'produces')]
    item_chair = models.CharField(max_length=20, choices=chair_choices, null=True)
    closet_choices = [(u'produces', u'produces')]
    item_closet = models.CharField(max_length=20, choices=closet_choices, null=True)
    couch_choices = [(u'produces', u'produces')]
    item_couch = models.CharField(max_length=20, choices=couch_choices, null=True)
    crib_choices = [(u'produces', u'produces')]
    item_crib = models.CharField(max_length=20, choices=crib_choices, null=True)
    door_choices = [(u'produces', u'produces')]
    item_door = models.CharField(max_length=20, choices=door_choices, null=True)
    drawer_choices = [(u'produces', u'produces')]
    item_drawer = models.CharField(max_length=20, choices=drawer_choices, null=True)
    dryer_choices = [(u'produces', u'produces')]
    item_dryer = models.CharField(max_length=20, choices=dryer_choices, null=True)
    garage_choices = [(u'produces', u'produces')]
    item_garage = models.CharField(max_length=20, choices=garage_choices, null=True)
    high_chair_choices = [(u'produces', u'produces')]
    item_high_chair = models.CharField(max_length=20, choices=high_chair_choices, null=True)
    kitchen_choices = [(u'produces', u'produces')]
    item_kitchen = models.CharField(max_length=20, choices=kitchen_choices, null=True)
    living_room_choices = [(u'produces', u'produces')]
    item_living_room = models.CharField(max_length=20, choices=living_room_choices, null=True)
    oven_choices = [(u'produces', u'produces')]
    item_oven = models.CharField(max_length=20, choices=oven_choices, null=True)
    play_pen_choices = [(u'produces', u'produces')]
    item_play_pen = models.CharField(max_length=20, choices=play_pen_choices, null=True)
    porch_choices = [(u'produces', u'produces')]
    item_porch = models.CharField(max_length=20, choices=porch_choices, null=True)
    potty_choices = [(u'produces', u'produces')]
    item_potty = models.CharField(max_length=20, choices=potty_choices, null=True)
    rocking_chair_choices = [(u'produces', u'produces')]
    item_rocking_chair = models.CharField(max_length=20, choices=rocking_chair_choices, null=True)
    refrigerator_choices = [(u'produces', u'produces')]
    item_refrigerator = models.CharField(max_length=20, choices=refrigerator_choices, null=True)
    room_choices = [(u'produces', u'produces')]
    item_room = models.CharField(max_length=20, choices=room_choices, null=True)
    shower_choices = [(u'produces', u'produces')]
    item_shower = models.CharField(max_length=20, choices=shower_choices, null=True)
    sink_choices = [(u'produces', u'produces')]
    item_sink = models.CharField(max_length=20, choices=sink_choices, null=True)
    sofa_choices = [(u'produces', u'produces')]
    item_sofa = models.CharField(max_length=20, choices=sofa_choices, null=True)
    stairs_choices = [(u'produces', u'produces')]
    item_stairs = models.CharField(max_length=20, choices=stairs_choices, null=True)
    stove_choices = [(u'produces', u'produces')]
    item_stove = models.CharField(max_length=20, choices=stove_choices, null=True)
    table_choices = [(u'produces', u'produces')]
    item_table = models.CharField(max_length=20, choices=table_choices, null=True)
    tv_choices = [(u'produces', u'produces')]
    item_tv = models.CharField(max_length=20, choices=tv_choices, null=True)
    window_choices = [(u'produces', u'produces')]
    item_window = models.CharField(max_length=20, choices=window_choices, null=True)
    washing_machine_choices = [(u'produces', u'produces')]
    item_washing_machine = models.CharField(max_length=20, choices=washing_machine_choices, null=True)
    backyard_choices = [(u'produces', u'produces')]
    item_backyard = models.CharField(max_length=20, choices=backyard_choices, null=True)
    cloud_choices = [(u'produces', u'produces')]
    item_cloud = models.CharField(max_length=20, choices=cloud_choices, null=True)
    flag_choices = [(u'produces', u'produces')]
    item_flag = models.CharField(max_length=20, choices=flag_choices, null=True)
    flower_choices = [(u'produces', u'produces')]
    item_flower = models.CharField(max_length=20, choices=flower_choices, null=True)
    garden_choices = [(u'produces', u'produces')]
    item_garden = models.CharField(max_length=20, choices=garden_choices, null=True)
    grass_choices = [(u'produces', u'produces')]
    item_grass = models.CharField(max_length=20, choices=grass_choices, null=True)
    hose_choices = [(u'produces', u'produces')]
    item_hose = models.CharField(max_length=20, choices=hose_choices, null=True)
    ladder_choices = [(u'produces', u'produces')]
    item_ladder = models.CharField(max_length=20, choices=ladder_choices, null=True)
    lawn_mower_choices = [(u'produces', u'produces')]
    item_lawn_mower = models.CharField(max_length=20, choices=lawn_mower_choices, null=True)
    moon_choices = [(u'produces', u'produces')]
    item_moon = models.CharField(max_length=20, choices=moon_choices, null=True)
    pool_choices = [(u'produces', u'produces')]
    item_pool = models.CharField(max_length=20, choices=pool_choices, null=True)
    rain_choices = [(u'produces', u'produces')]
    item_rain = models.CharField(max_length=20, choices=rain_choices, null=True)
    rock_choices = [(u'produces', u'produces')]
    item_rock = models.CharField(max_length=20, choices=rock_choices, null=True)
    roof_choices = [(u'produces', u'produces')]
    item_roof = models.CharField(max_length=20, choices=roof_choices, null=True)
    sandbox_choices = [(u'produces', u'produces')]
    item_sandbox = models.CharField(max_length=20, choices=sandbox_choices, null=True)
    shovel_choices = [(u'produces', u'produces')]
    item_shovel = models.CharField(max_length=20, choices=shovel_choices, null=True)
    sidewalk_choices = [(u'produces', u'produces')]
    item_sidewalk = models.CharField(max_length=20, choices=sidewalk_choices, null=True)
    sky_choices = [(u'produces', u'produces')]
    item_sky = models.CharField(max_length=20, choices=sky_choices, null=True)
    slide_object_choices = [(u'produces', u'produces')]
    item_slide_object = models.CharField(max_length=20, choices=slide_object_choices, null=True)
    snow_choices = [(u'produces', u'produces')]
    item_snow = models.CharField(max_length=20, choices=snow_choices, null=True)
    snowman_choices = [(u'produces', u'produces')]
    item_snowman = models.CharField(max_length=20, choices=snowman_choices, null=True)
    sprinkler_choices = [(u'produces', u'produces')]
    item_sprinkler = models.CharField(max_length=20, choices=sprinkler_choices, null=True)
    star_choices = [(u'produces', u'produces')]
    item_star = models.CharField(max_length=20, choices=star_choices, null=True)
    stick_choices = [(u'produces', u'produces')]
    item_stick = models.CharField(max_length=20, choices=stick_choices, null=True)
    stone_choices = [(u'produces', u'produces')]
    item_stone = models.CharField(max_length=20, choices=stone_choices, null=True)
    street_choices = [(u'produces', u'produces')]
    item_street = models.CharField(max_length=20, choices=street_choices, null=True)
    sun_choices = [(u'produces', u'produces')]
    item_sun = models.CharField(max_length=20, choices=sun_choices, null=True)
    swing_object_choices = [(u'produces', u'produces')]
    item_swing_object = models.CharField(max_length=20, choices=swing_object_choices, null=True)
    tree_choices = [(u'produces', u'produces')]
    item_tree = models.CharField(max_length=20, choices=tree_choices, null=True)
    water_not_beverage_choices = [(u'produces', u'produces')]
    item_water_not_beverage = models.CharField(max_length=20, choices=water_not_beverage_choices, null=True)
    wind_choices = [(u'produces', u'produces')]
    item_wind = models.CharField(max_length=20, choices=wind_choices, null=True)
    beach_choices = [(u'produces', u'produces')]
    item_beach = models.CharField(max_length=20, choices=beach_choices, null=True)
    camping_choices = [(u'produces', u'produces')]
    item_camping = models.CharField(max_length=20, choices=camping_choices, null=True)
    church_choices = [(u'produces', u'produces')]
    item_church = models.CharField(max_length=20, choices=church_choices, null=True)
    circus_choices = [(u'produces', u'produces')]
    item_circus = models.CharField(max_length=20, choices=circus_choices, null=True)
    country_choices = [(u'produces', u'produces')]
    item_country = models.CharField(max_length=20, choices=country_choices, null=True)
    downtown_choices = [(u'produces', u'produces')]
    item_downtown = models.CharField(max_length=20, choices=downtown_choices, null=True)
    farm_choices = [(u'produces', u'produces')]
    item_farm = models.CharField(max_length=20, choices=farm_choices, null=True)
    gas_station_choices = [(u'produces', u'produces')]
    item_gas_station = models.CharField(max_length=20, choices=gas_station_choices, null=True)
    home_choices = [(u'produces', u'produces')]
    item_home = models.CharField(max_length=20, choices=home_choices, null=True)
    house_choices = [(u'produces', u'produces')]
    item_house = models.CharField(max_length=20, choices=house_choices, null=True)
    movie_choices = [(u'produces', u'produces')]
    item_movie = models.CharField(max_length=20, choices=movie_choices, null=True)
    outside_choices = [(u'produces', u'produces')]
    item_outside = models.CharField(max_length=20, choices=outside_choices, null=True)
    park_choices = [(u'produces', u'produces')]
    item_park = models.CharField(max_length=20, choices=park_choices, null=True)
    party_choices = [(u'produces', u'produces')]
    item_party = models.CharField(max_length=20, choices=party_choices, null=True)
    picnic_choices = [(u'produces', u'produces')]
    item_picnic = models.CharField(max_length=20, choices=picnic_choices, null=True)
    playground_choices = [(u'produces', u'produces')]
    item_playground = models.CharField(max_length=20, choices=playground_choices, null=True)
    school_choices = [(u'produces', u'produces')]
    item_school = models.CharField(max_length=20, choices=school_choices, null=True)
    store_choices = [(u'produces', u'produces')]
    item_store = models.CharField(max_length=20, choices=store_choices, null=True)
    woods_choices = [(u'produces', u'produces')]
    item_woods = models.CharField(max_length=20, choices=woods_choices, null=True)
    work_place_choices = [(u'produces', u'produces')]
    item_work_place = models.CharField(max_length=20, choices=work_place_choices, null=True)
    yard_choices = [(u'produces', u'produces')]
    item_yard = models.CharField(max_length=20, choices=yard_choices, null=True)
    zoo_choices = [(u'produces', u'produces')]
    item_zoo = models.CharField(max_length=20, choices=zoo_choices, null=True)
    aunt_choices = [(u'produces', u'produces')]
    item_aunt = models.CharField(max_length=20, choices=aunt_choices, null=True)
    baby_choices = [(u'produces', u'produces')]
    item_baby = models.CharField(max_length=20, choices=baby_choices, null=True)
    babysitter_choices = [(u'produces', u'produces')]
    item_babysitter = models.CharField(max_length=20, choices=babysitter_choices, null=True)
    babysitter_name_choices = [(u'produces', u'produces')]
    item_babysitter_name = models.CharField(max_length=20, choices=babysitter_name_choices, null=True)
    boy_choices = [(u'produces', u'produces')]
    item_boy = models.CharField(max_length=20, choices=boy_choices, null=True)
    brother_choices = [(u'produces', u'produces')]
    item_brother = models.CharField(max_length=20, choices=brother_choices, null=True)
    child_choices = [(u'produces', u'produces')]
    item_child = models.CharField(max_length=20, choices=child_choices, null=True)
    clown_choices = [(u'produces', u'produces')]
    item_clown = models.CharField(max_length=20, choices=clown_choices, null=True)
    cowboy_choices = [(u'produces', u'produces')]
    item_cowboy = models.CharField(max_length=20, choices=cowboy_choices, null=True)
    daddy_choices = [(u'produces', u'produces')]
    item_daddy = models.CharField(max_length=20, choices=daddy_choices, null=True)
    doctor_choices = [(u'produces', u'produces')]
    item_doctor = models.CharField(max_length=20, choices=doctor_choices, null=True)
    fireman_choices = [(u'produces', u'produces')]
    item_fireman = models.CharField(max_length=20, choices=fireman_choices, null=True)
    friend_choices = [(u'produces', u'produces')]
    item_friend = models.CharField(max_length=20, choices=friend_choices, null=True)
    girl_choices = [(u'produces', u'produces')]
    item_girl = models.CharField(max_length=20, choices=girl_choices, null=True)
    grandma_choices = [(u'produces', u'produces')]
    item_grandma = models.CharField(max_length=20, choices=grandma_choices, null=True)
    grandpa_choices = [(u'produces', u'produces')]
    item_grandpa = models.CharField(max_length=20, choices=grandpa_choices, null=True)
    lady_choices = [(u'produces', u'produces')]
    item_lady = models.CharField(max_length=20, choices=lady_choices, null=True)
    mailman_choices = [(u'produces', u'produces')]
    item_mailman = models.CharField(max_length=20, choices=mailman_choices, null=True)
    man_choices = [(u'produces', u'produces')]
    item_man = models.CharField(max_length=20, choices=man_choices, null=True)
    mommy_choices = [(u'produces', u'produces')]
    item_mommy = models.CharField(max_length=20, choices=mommy_choices, null=True)
    nurse_choices = [(u'produces', u'produces')]
    item_nurse = models.CharField(max_length=20, choices=nurse_choices, null=True)
    child_own_name_choices = [(u'produces', u'produces')]
    item_child_own_name = models.CharField(max_length=20, choices=child_own_name_choices, null=True)
    people_choices = [(u'produces', u'produces')]
    item_people = models.CharField(max_length=20, choices=people_choices, null=True)
    person_choices = [(u'produces', u'produces')]
    item_person = models.CharField(max_length=20, choices=person_choices, null=True)
    pet_name_choices = [(u'produces', u'produces')]
    item_pet_name = models.CharField(max_length=20, choices=pet_name_choices, null=True)
    police_choices = [(u'produces', u'produces')]
    item_police = models.CharField(max_length=20, choices=police_choices, null=True)
    sister_choices = [(u'produces', u'produces')]
    item_sister = models.CharField(max_length=20, choices=sister_choices, null=True)
    teacher_choices = [(u'produces', u'produces')]
    item_teacher = models.CharField(max_length=20, choices=teacher_choices, null=True)
    uncle_choices = [(u'produces', u'produces')]
    item_uncle = models.CharField(max_length=20, choices=uncle_choices, null=True)
    bath_choices = [(u'produces', u'produces')]
    item_bath = models.CharField(max_length=20, choices=bath_choices, null=True)
    breakfast_choices = [(u'produces', u'produces')]
    item_breakfast = models.CharField(max_length=20, choices=breakfast_choices, null=True)
    bye_choices = [(u'produces', u'produces')]
    item_bye = models.CharField(max_length=20, choices=bye_choices, null=True)
    call_choices = [(u'produces', u'produces')]
    item_call = models.CharField(max_length=20, choices=call_choices, null=True)
    dinner_choices = [(u'produces', u'produces')]
    item_dinner = models.CharField(max_length=20, choices=dinner_choices, null=True)
    give_me_five_choices = [(u'produces', u'produces')]
    item_give_me_five = models.CharField(max_length=20, choices=give_me_five_choices, null=True)
    gonna_get_you_choices = [(u'produces', u'produces')]
    item_gonna_get_you = models.CharField(max_length=20, choices=gonna_get_you_choices, null=True)
    go_potty_choices = [(u'produces', u'produces')]
    item_go_potty = models.CharField(max_length=20, choices=go_potty_choices, null=True)
    hello_choices = [(u'produces', u'produces')]
    item_hello = models.CharField(max_length=20, choices=hello_choices, null=True)
    hi_choices = [(u'produces', u'produces')]
    item_hi = models.CharField(max_length=20, choices=hi_choices, null=True)
    lunch_choices = [(u'produces', u'produces')]
    item_lunch = models.CharField(max_length=20, choices=lunch_choices, null=True)
    nap_choices = [(u'produces', u'produces')]
    item_nap = models.CharField(max_length=20, choices=nap_choices, null=True)
    nightnight_choices = [(u'produces', u'produces')]
    item_nightnight = models.CharField(max_length=20, choices=nightnight_choices, null=True)
    no_choices = [(u'produces', u'produces')]
    item_no = models.CharField(max_length=20, choices=no_choices, null=True)
    pattycake_choices = [(u'produces', u'produces')]
    item_pattycake = models.CharField(max_length=20, choices=pattycake_choices, null=True)
    peekaboo_choices = [(u'produces', u'produces')]
    item_peekaboo = models.CharField(max_length=20, choices=peekaboo_choices, null=True)
    please_choices = [(u'produces', u'produces')]
    item_please = models.CharField(max_length=20, choices=please_choices, null=True)
    shh_choices = [(u'produces', u'produces')]
    item_shh = models.CharField(max_length=20, choices=shh_choices, null=True)
    shopping_choices = [(u'produces', u'produces')]
    item_shopping = models.CharField(max_length=20, choices=shopping_choices, null=True)
    snack_choices = [(u'produces', u'produces')]
    item_snack = models.CharField(max_length=20, choices=snack_choices, null=True)
    so_big_choices = [(u'produces', u'produces')]
    item_so_big = models.CharField(max_length=20, choices=so_big_choices, null=True)
    thank_you_choices = [(u'produces', u'produces')]
    item_thank_you = models.CharField(max_length=20, choices=thank_you_choices, null=True)
    this_little_piggy_choices = [(u'produces', u'produces')]
    item_this_little_piggy = models.CharField(max_length=20, choices=this_little_piggy_choices, null=True)
    turn_around_choices = [(u'produces', u'produces')]
    item_turn_around = models.CharField(max_length=20, choices=turn_around_choices, null=True)
    yes_choices = [(u'produces', u'produces')]
    item_yes = models.CharField(max_length=20, choices=yes_choices, null=True)
    bite_choices = [(u'produces', u'produces')]
    item_bite = models.CharField(max_length=20, choices=bite_choices, null=True)
    blow_choices = [(u'produces', u'produces')]
    item_blow = models.CharField(max_length=20, choices=blow_choices, null=True)
    break_choices = [(u'produces', u'produces')]
    item_break = models.CharField(max_length=20, choices=break_choices, null=True)
    bring_choices = [(u'produces', u'produces')]
    item_bring = models.CharField(max_length=20, choices=bring_choices, null=True)
    build_choices = [(u'produces', u'produces')]
    item_build = models.CharField(max_length=20, choices=build_choices, null=True)
    bump_choices = [(u'produces', u'produces')]
    item_bump = models.CharField(max_length=20, choices=bump_choices, null=True)
    buy_choices = [(u'produces', u'produces')]
    item_buy = models.CharField(max_length=20, choices=buy_choices, null=True)
    carry_choices = [(u'produces', u'produces')]
    item_carry = models.CharField(max_length=20, choices=carry_choices, null=True)
    catch_choices = [(u'produces', u'produces')]
    item_catch = models.CharField(max_length=20, choices=catch_choices, null=True)
    chase_choices = [(u'produces', u'produces')]
    item_chase = models.CharField(max_length=20, choices=chase_choices, null=True)
    clap_choices = [(u'produces', u'produces')]
    item_clap = models.CharField(max_length=20, choices=clap_choices, null=True)
    clean_action_choices = [(u'produces', u'produces')]
    item_clean_action = models.CharField(max_length=20, choices=clean_action_choices, null=True)
    climb_choices = [(u'produces', u'produces')]
    item_climb = models.CharField(max_length=20, choices=climb_choices, null=True)
    close_choices = [(u'produces', u'produces')]
    item_close = models.CharField(max_length=20, choices=close_choices, null=True)
    cook_choices = [(u'produces', u'produces')]
    item_cook = models.CharField(max_length=20, choices=cook_choices, null=True)
    cover_choices = [(u'produces', u'produces')]
    item_cover = models.CharField(max_length=20, choices=cover_choices, null=True)
    cry_choices = [(u'produces', u'produces')]
    item_cry = models.CharField(max_length=20, choices=cry_choices, null=True)
    cut_choices = [(u'produces', u'produces')]
    item_cut = models.CharField(max_length=20, choices=cut_choices, null=True)
    dance_choices = [(u'produces', u'produces')]
    item_dance = models.CharField(max_length=20, choices=dance_choices, null=True)
    draw_choices = [(u'produces', u'produces')]
    item_draw = models.CharField(max_length=20, choices=draw_choices, null=True)
    drink_action_choices = [(u'produces', u'produces')]
    item_drink_action = models.CharField(max_length=20, choices=drink_action_choices, null=True)
    drive_choices = [(u'produces', u'produces')]
    item_drive = models.CharField(max_length=20, choices=drive_choices, null=True)
    drop_choices = [(u'produces', u'produces')]
    item_drop = models.CharField(max_length=20, choices=drop_choices, null=True)
    dry_action_choices = [(u'produces', u'produces')]
    item_dry_action = models.CharField(max_length=20, choices=dry_action_choices, null=True)
    dump_choices = [(u'produces', u'produces')]
    item_dump = models.CharField(max_length=20, choices=dump_choices, null=True)
    eat_choices = [(u'produces', u'produces')]
    item_eat = models.CharField(max_length=20, choices=eat_choices, null=True)
    fall_choices = [(u'produces', u'produces')]
    item_fall = models.CharField(max_length=20, choices=fall_choices, null=True)
    feed_choices = [(u'produces', u'produces')]
    item_feed = models.CharField(max_length=20, choices=feed_choices, null=True)
    find_choices = [(u'produces', u'produces')]
    item_find = models.CharField(max_length=20, choices=find_choices, null=True)
    finish_choices = [(u'produces', u'produces')]
    item_finish = models.CharField(max_length=20, choices=finish_choices, null=True)
    fit_choices = [(u'produces', u'produces')]
    item_fit = models.CharField(max_length=20, choices=fit_choices, null=True)
    fix_choices = [(u'produces', u'produces')]
    item_fix = models.CharField(max_length=20, choices=fix_choices, null=True)
    get_choices = [(u'produces', u'produces')]
    item_get = models.CharField(max_length=20, choices=get_choices, null=True)
    give_choices = [(u'produces', u'produces')]
    item_give = models.CharField(max_length=20, choices=give_choices, null=True)
    go_choices = [(u'produces', u'produces')]
    item_go = models.CharField(max_length=20, choices=go_choices, null=True)
    hate_choices = [(u'produces', u'produces')]
    item_hate = models.CharField(max_length=20, choices=hate_choices, null=True)
    have_choices = [(u'produces', u'produces')]
    item_have = models.CharField(max_length=20, choices=have_choices, null=True)
    hear_choices = [(u'produces', u'produces')]
    item_hear = models.CharField(max_length=20, choices=hear_choices, null=True)
    help_choices = [(u'produces', u'produces')]
    item_help = models.CharField(max_length=20, choices=help_choices, null=True)
    hide_choices = [(u'produces', u'produces')]
    item_hide = models.CharField(max_length=20, choices=hide_choices, null=True)
    hit_choices = [(u'produces', u'produces')]
    item_hit = models.CharField(max_length=20, choices=hit_choices, null=True)
    hold_choices = [(u'produces', u'produces')]
    item_hold = models.CharField(max_length=20, choices=hold_choices, null=True)
    hug_choices = [(u'produces', u'produces')]
    item_hug = models.CharField(max_length=20, choices=hug_choices, null=True)
    hurry_choices = [(u'produces', u'produces')]
    item_hurry = models.CharField(max_length=20, choices=hurry_choices, null=True)
    jump_choices = [(u'produces', u'produces')]
    item_jump = models.CharField(max_length=20, choices=jump_choices, null=True)
    kick_choices = [(u'produces', u'produces')]
    item_kick = models.CharField(max_length=20, choices=kick_choices, null=True)
    kiss_choices = [(u'produces', u'produces')]
    item_kiss = models.CharField(max_length=20, choices=kiss_choices, null=True)
    knock_choices = [(u'produces', u'produces')]
    item_knock = models.CharField(max_length=20, choices=knock_choices, null=True)
    lick_choices = [(u'produces', u'produces')]
    item_lick = models.CharField(max_length=20, choices=lick_choices, null=True)
    like_choices = [(u'produces', u'produces')]
    item_like = models.CharField(max_length=20, choices=like_choices, null=True)
    listen_choices = [(u'produces', u'produces')]
    item_listen = models.CharField(max_length=20, choices=listen_choices, null=True)
    look_choices = [(u'produces', u'produces')]
    item_look = models.CharField(max_length=20, choices=look_choices, null=True)
    love_choices = [(u'produces', u'produces')]
    item_love = models.CharField(max_length=20, choices=love_choices, null=True)
    make_choices = [(u'produces', u'produces')]
    item_make = models.CharField(max_length=20, choices=make_choices, null=True)
    open_choices = [(u'produces', u'produces')]
    item_open = models.CharField(max_length=20, choices=open_choices, null=True)
    paint_choices = [(u'produces', u'produces')]
    item_paint = models.CharField(max_length=20, choices=paint_choices, null=True)
    pick_choices = [(u'produces', u'produces')]
    item_pick = models.CharField(max_length=20, choices=pick_choices, null=True)
    play_choices = [(u'produces', u'produces')]
    item_play = models.CharField(max_length=20, choices=play_choices, null=True)
    pour_choices = [(u'produces', u'produces')]
    item_pour = models.CharField(max_length=20, choices=pour_choices, null=True)
    pretend_choices = [(u'produces', u'produces')]
    item_pretend = models.CharField(max_length=20, choices=pretend_choices, null=True)
    pull_choices = [(u'produces', u'produces')]
    item_pull = models.CharField(max_length=20, choices=pull_choices, null=True)
    push_choices = [(u'produces', u'produces')]
    item_push = models.CharField(max_length=20, choices=push_choices, null=True)
    put_choices = [(u'produces', u'produces')]
    item_put = models.CharField(max_length=20, choices=put_choices, null=True)
    read_choices = [(u'produces', u'produces')]
    item_read = models.CharField(max_length=20, choices=read_choices, null=True)
    ride_choices = [(u'produces', u'produces')]
    item_ride = models.CharField(max_length=20, choices=ride_choices, null=True)
    rip_choices = [(u'produces', u'produces')]
    item_rip = models.CharField(max_length=20, choices=rip_choices, null=True)
    run_choices = [(u'produces', u'produces')]
    item_run = models.CharField(max_length=20, choices=run_choices, null=True)
    say_choices = [(u'produces', u'produces')]
    item_say = models.CharField(max_length=20, choices=say_choices, null=True)
    see_choices = [(u'produces', u'produces')]
    item_see = models.CharField(max_length=20, choices=see_choices, null=True)
    shake_choices = [(u'produces', u'produces')]
    item_shake = models.CharField(max_length=20, choices=shake_choices, null=True)
    share_choices = [(u'produces', u'produces')]
    item_share = models.CharField(max_length=20, choices=share_choices, null=True)
    show_choices = [(u'produces', u'produces')]
    item_show = models.CharField(max_length=20, choices=show_choices, null=True)
    sing_choices = [(u'produces', u'produces')]
    item_sing = models.CharField(max_length=20, choices=sing_choices, null=True)
    sit_choices = [(u'produces', u'produces')]
    item_sit = models.CharField(max_length=20, choices=sit_choices, null=True)
    skate_choices = [(u'produces', u'produces')]
    item_skate = models.CharField(max_length=20, choices=skate_choices, null=True)
    sleep_choices = [(u'produces', u'produces')]
    item_sleep = models.CharField(max_length=20, choices=sleep_choices, null=True)
    slide_action_choices = [(u'produces', u'produces')]
    item_slide_action = models.CharField(max_length=20, choices=slide_action_choices, null=True)
    smile_choices = [(u'produces', u'produces')]
    item_smile = models.CharField(max_length=20, choices=smile_choices, null=True)
    spill_choices = [(u'produces', u'produces')]
    item_spill = models.CharField(max_length=20, choices=spill_choices, null=True)
    splash_choices = [(u'produces', u'produces')]
    item_splash = models.CharField(max_length=20, choices=splash_choices, null=True)
    stand_choices = [(u'produces', u'produces')]
    item_stand = models.CharField(max_length=20, choices=stand_choices, null=True)
    stay_choices = [(u'produces', u'produces')]
    item_stay = models.CharField(max_length=20, choices=stay_choices, null=True)
    stop_choices = [(u'produces', u'produces')]
    item_stop = models.CharField(max_length=20, choices=stop_choices, null=True)
    sweep_choices = [(u'produces', u'produces')]
    item_sweep = models.CharField(max_length=20, choices=sweep_choices, null=True)
    swim_choices = [(u'produces', u'produces')]
    item_swim = models.CharField(max_length=20, choices=swim_choices, null=True)
    swing_action_choices = [(u'produces', u'produces')]
    item_swing_action = models.CharField(max_length=20, choices=swing_action_choices, null=True)
    take_choices = [(u'produces', u'produces')]
    item_take = models.CharField(max_length=20, choices=take_choices, null=True)
    talk_choices = [(u'produces', u'produces')]
    item_talk = models.CharField(max_length=20, choices=talk_choices, null=True)
    taste_choices = [(u'produces', u'produces')]
    item_taste = models.CharField(max_length=20, choices=taste_choices, null=True)
    tear_choices = [(u'produces', u'produces')]
    item_tear = models.CharField(max_length=20, choices=tear_choices, null=True)
    think_choices = [(u'produces', u'produces')]
    item_think = models.CharField(max_length=20, choices=think_choices, null=True)
    throw_choices = [(u'produces', u'produces')]
    item_throw = models.CharField(max_length=20, choices=throw_choices, null=True)
    tickle_choices = [(u'produces', u'produces')]
    item_tickle = models.CharField(max_length=20, choices=tickle_choices, null=True)
    touch_choices = [(u'produces', u'produces')]
    item_touch = models.CharField(max_length=20, choices=touch_choices, null=True)
    wait_choices = [(u'produces', u'produces')]
    item_wait = models.CharField(max_length=20, choices=wait_choices, null=True)
    wake_choices = [(u'produces', u'produces')]
    item_wake = models.CharField(max_length=20, choices=wake_choices, null=True)
    walk_choices = [(u'produces', u'produces')]
    item_walk = models.CharField(max_length=20, choices=walk_choices, null=True)
    wash_choices = [(u'produces', u'produces')]
    item_wash = models.CharField(max_length=20, choices=wash_choices, null=True)
    watch_action_choices = [(u'produces', u'produces')]
    item_watch_action = models.CharField(max_length=20, choices=watch_action_choices, null=True)
    wipe_choices = [(u'produces', u'produces')]
    item_wipe = models.CharField(max_length=20, choices=wipe_choices, null=True)
    wish_choices = [(u'produces', u'produces')]
    item_wish = models.CharField(max_length=20, choices=wish_choices, null=True)
    work_action_choices = [(u'produces', u'produces')]
    item_work_action = models.CharField(max_length=20, choices=work_action_choices, null=True)
    write_choices = [(u'produces', u'produces')]
    item_write = models.CharField(max_length=20, choices=write_choices, null=True)
    allgone_choices = [(u'produces', u'produces')]
    item_allgone = models.CharField(max_length=20, choices=allgone_choices, null=True)
    asleep_choices = [(u'produces', u'produces')]
    item_asleep = models.CharField(max_length=20, choices=asleep_choices, null=True)
    awake_choices = [(u'produces', u'produces')]
    item_awake = models.CharField(max_length=20, choices=awake_choices, null=True)
    bad_choices = [(u'produces', u'produces')]
    item_bad = models.CharField(max_length=20, choices=bad_choices, null=True)
    better_choices = [(u'produces', u'produces')]
    item_better = models.CharField(max_length=20, choices=better_choices, null=True)
    big_choices = [(u'produces', u'produces')]
    item_big = models.CharField(max_length=20, choices=big_choices, null=True)
    black_choices = [(u'produces', u'produces')]
    item_black = models.CharField(max_length=20, choices=black_choices, null=True)
    blue_choices = [(u'produces', u'produces')]
    item_blue = models.CharField(max_length=20, choices=blue_choices, null=True)
    broken_choices = [(u'produces', u'produces')]
    item_broken = models.CharField(max_length=20, choices=broken_choices, null=True)
    brown_choices = [(u'produces', u'produces')]
    item_brown = models.CharField(max_length=20, choices=brown_choices, null=True)
    careful_choices = [(u'produces', u'produces')]
    item_careful = models.CharField(max_length=20, choices=careful_choices, null=True)
    clean_description_choices = [(u'produces', u'produces')]
    item_clean_description = models.CharField(max_length=20, choices=clean_description_choices, null=True)
    cold_choices = [(u'produces', u'produces')]
    item_cold = models.CharField(max_length=20, choices=cold_choices, null=True)
    cute_choices = [(u'produces', u'produces')]
    item_cute = models.CharField(max_length=20, choices=cute_choices, null=True)
    dark_choices = [(u'produces', u'produces')]
    item_dark = models.CharField(max_length=20, choices=dark_choices, null=True)
    dirty_choices = [(u'produces', u'produces')]
    item_dirty = models.CharField(max_length=20, choices=dirty_choices, null=True)
    dry_description_choices = [(u'produces', u'produces')]
    item_dry_description = models.CharField(max_length=20, choices=dry_description_choices, null=True)
    empty_choices = [(u'produces', u'produces')]
    item_empty = models.CharField(max_length=20, choices=empty_choices, null=True)
    fast_choices = [(u'produces', u'produces')]
    item_fast = models.CharField(max_length=20, choices=fast_choices, null=True)
    fine_choices = [(u'produces', u'produces')]
    item_fine = models.CharField(max_length=20, choices=fine_choices, null=True)
    first_choices = [(u'produces', u'produces')]
    item_first = models.CharField(max_length=20, choices=first_choices, null=True)
    full_choices = [(u'produces', u'produces')]
    item_full = models.CharField(max_length=20, choices=full_choices, null=True)
    gentle_choices = [(u'produces', u'produces')]
    item_gentle = models.CharField(max_length=20, choices=gentle_choices, null=True)
    good_choices = [(u'produces', u'produces')]
    item_good = models.CharField(max_length=20, choices=good_choices, null=True)
    green_choices = [(u'produces', u'produces')]
    item_green = models.CharField(max_length=20, choices=green_choices, null=True)
    happy_choices = [(u'produces', u'produces')]
    item_happy = models.CharField(max_length=20, choices=happy_choices, null=True)
    hard_choices = [(u'produces', u'produces')]
    item_hard = models.CharField(max_length=20, choices=hard_choices, null=True)
    heavy_choices = [(u'produces', u'produces')]
    item_heavy = models.CharField(max_length=20, choices=heavy_choices, null=True)
    high_choices = [(u'produces', u'produces')]
    item_high = models.CharField(max_length=20, choices=high_choices, null=True)
    hot_choices = [(u'produces', u'produces')]
    item_hot = models.CharField(max_length=20, choices=hot_choices, null=True)
    hungry_choices = [(u'produces', u'produces')]
    item_hungry = models.CharField(max_length=20, choices=hungry_choices, null=True)
    hurt_choices = [(u'produces', u'produces')]
    item_hurt = models.CharField(max_length=20, choices=hurt_choices, null=True)
    last_choices = [(u'produces', u'produces')]
    item_last = models.CharField(max_length=20, choices=last_choices, null=True)
    little_choices = [(u'produces', u'produces')]
    item_little = models.CharField(max_length=20, choices=little_choices, null=True)
    long_choices = [(u'produces', u'produces')]
    item_long = models.CharField(max_length=20, choices=long_choices, null=True)
    loud_choices = [(u'produces', u'produces')]
    item_loud = models.CharField(max_length=20, choices=loud_choices, null=True)
    mad_choices = [(u'produces', u'produces')]
    item_mad = models.CharField(max_length=20, choices=mad_choices, null=True)
    naughty_choices = [(u'produces', u'produces')]
    item_naughty = models.CharField(max_length=20, choices=naughty_choices, null=True)
    new_choices = [(u'produces', u'produces')]
    item_new = models.CharField(max_length=20, choices=new_choices, null=True)
    nice_choices = [(u'produces', u'produces')]
    item_nice = models.CharField(max_length=20, choices=nice_choices, null=True)
    noisy_choices = [(u'produces', u'produces')]
    item_noisy = models.CharField(max_length=20, choices=noisy_choices, null=True)
    old_choices = [(u'produces', u'produces')]
    item_old = models.CharField(max_length=20, choices=old_choices, null=True)
    orange_description_choices = [(u'produces', u'produces')]
    item_orange_description = models.CharField(max_length=20, choices=orange_description_choices, null=True)
    poor_choices = [(u'produces', u'produces')]
    item_poor = models.CharField(max_length=20, choices=poor_choices, null=True)
    pretty_choices = [(u'produces', u'produces')]
    item_pretty = models.CharField(max_length=20, choices=pretty_choices, null=True)
    quiet_choices = [(u'produces', u'produces')]
    item_quiet = models.CharField(max_length=20, choices=quiet_choices, null=True)
    red_choices = [(u'produces', u'produces')]
    item_red = models.CharField(max_length=20, choices=red_choices, null=True)
    sad_choices = [(u'produces', u'produces')]
    item_sad = models.CharField(max_length=20, choices=sad_choices, null=True)
    scared_choices = [(u'produces', u'produces')]
    item_scared = models.CharField(max_length=20, choices=scared_choices, null=True)
    sick_choices = [(u'produces', u'produces')]
    item_sick = models.CharField(max_length=20, choices=sick_choices, null=True)
    sleepy_choices = [(u'produces', u'produces')]
    item_sleepy = models.CharField(max_length=20, choices=sleepy_choices, null=True)
    slow_choices = [(u'produces', u'produces')]
    item_slow = models.CharField(max_length=20, choices=slow_choices, null=True)
    soft_choices = [(u'produces', u'produces')]
    item_soft = models.CharField(max_length=20, choices=soft_choices, null=True)
    sticky_choices = [(u'produces', u'produces')]
    item_sticky = models.CharField(max_length=20, choices=sticky_choices, null=True)
    stuck_choices = [(u'produces', u'produces')]
    item_stuck = models.CharField(max_length=20, choices=stuck_choices, null=True)
    thirsty_choices = [(u'produces', u'produces')]
    item_thirsty = models.CharField(max_length=20, choices=thirsty_choices, null=True)
    tiny_choices = [(u'produces', u'produces')]
    item_tiny = models.CharField(max_length=20, choices=tiny_choices, null=True)
    tired_choices = [(u'produces', u'produces')]
    item_tired = models.CharField(max_length=20, choices=tired_choices, null=True)
    wet_choices = [(u'produces', u'produces')]
    item_wet = models.CharField(max_length=20, choices=wet_choices, null=True)
    white_choices = [(u'produces', u'produces')]
    item_white = models.CharField(max_length=20, choices=white_choices, null=True)
    windy_choices = [(u'produces', u'produces')]
    item_windy = models.CharField(max_length=20, choices=windy_choices, null=True)
    yellow_choices = [(u'produces', u'produces')]
    item_yellow = models.CharField(max_length=20, choices=yellow_choices, null=True)
    yucky_choices = [(u'produces', u'produces')]
    item_yucky = models.CharField(max_length=20, choices=yucky_choices, null=True)
    after_choices = [(u'produces', u'produces')]
    item_after = models.CharField(max_length=20, choices=after_choices, null=True)
    before_choices = [(u'produces', u'produces')]
    item_before = models.CharField(max_length=20, choices=before_choices, null=True)
    day_choices = [(u'produces', u'produces')]
    item_day = models.CharField(max_length=20, choices=day_choices, null=True)
    later_choices = [(u'produces', u'produces')]
    item_later = models.CharField(max_length=20, choices=later_choices, null=True)
    morning_choices = [(u'produces', u'produces')]
    item_morning = models.CharField(max_length=20, choices=morning_choices, null=True)
    night_choices = [(u'produces', u'produces')]
    item_night = models.CharField(max_length=20, choices=night_choices, null=True)
    now_choices = [(u'produces', u'produces')]
    item_now = models.CharField(max_length=20, choices=now_choices, null=True)
    time_choices = [(u'produces', u'produces')]
    item_time = models.CharField(max_length=20, choices=time_choices, null=True)
    today_choices = [(u'produces', u'produces')]
    item_today = models.CharField(max_length=20, choices=today_choices, null=True)
    tomorrow_choices = [(u'produces', u'produces')]
    item_tomorrow = models.CharField(max_length=20, choices=tomorrow_choices, null=True)
    tonight_choices = [(u'produces', u'produces')]
    item_tonight = models.CharField(max_length=20, choices=tonight_choices, null=True)
    yesterday_choices = [(u'produces', u'produces')]
    item_yesterday = models.CharField(max_length=20, choices=yesterday_choices, null=True)
    he_choices = [(u'produces', u'produces')]
    item_he = models.CharField(max_length=20, choices=he_choices, null=True)
    her_choices = [(u'produces', u'produces')]
    item_her = models.CharField(max_length=20, choices=her_choices, null=True)
    hers_choices = [(u'produces', u'produces')]
    item_hers = models.CharField(max_length=20, choices=hers_choices, null=True)
    him_choices = [(u'produces', u'produces')]
    item_him = models.CharField(max_length=20, choices=him_choices, null=True)
    his_choices = [(u'produces', u'produces')]
    item_his = models.CharField(max_length=20, choices=his_choices, null=True)
    i_choices = [(u'produces', u'produces')]
    item_i = models.CharField(max_length=20, choices=i_choices, null=True)
    it_choices = [(u'produces', u'produces')]
    item_it = models.CharField(max_length=20, choices=it_choices, null=True)
    me_choices = [(u'produces', u'produces')]
    item_me = models.CharField(max_length=20, choices=me_choices, null=True)
    mine_choices = [(u'produces', u'produces')]
    item_mine = models.CharField(max_length=20, choices=mine_choices, null=True)
    my_choices = [(u'produces', u'produces')]
    item_my = models.CharField(max_length=20, choices=my_choices, null=True)
    myself_choices = [(u'produces', u'produces')]
    item_myself = models.CharField(max_length=20, choices=myself_choices, null=True)
    our_choices = [(u'produces', u'produces')]
    item_our = models.CharField(max_length=20, choices=our_choices, null=True)
    she_choices = [(u'produces', u'produces')]
    item_she = models.CharField(max_length=20, choices=she_choices, null=True)
    that_choices = [(u'produces', u'produces')]
    item_that = models.CharField(max_length=20, choices=that_choices, null=True)
    their_choices = [(u'produces', u'produces')]
    item_their = models.CharField(max_length=20, choices=their_choices, null=True)
    them_choices = [(u'produces', u'produces')]
    item_them = models.CharField(max_length=20, choices=them_choices, null=True)
    these_choices = [(u'produces', u'produces')]
    item_these = models.CharField(max_length=20, choices=these_choices, null=True)
    they_choices = [(u'produces', u'produces')]
    item_they = models.CharField(max_length=20, choices=they_choices, null=True)
    this_choices = [(u'produces', u'produces')]
    item_this = models.CharField(max_length=20, choices=this_choices, null=True)
    those_choices = [(u'produces', u'produces')]
    item_those = models.CharField(max_length=20, choices=those_choices, null=True)
    us_choices = [(u'produces', u'produces')]
    item_us = models.CharField(max_length=20, choices=us_choices, null=True)
    we_choices = [(u'produces', u'produces')]
    item_we = models.CharField(max_length=20, choices=we_choices, null=True)
    you_choices = [(u'produces', u'produces')]
    item_you = models.CharField(max_length=20, choices=you_choices, null=True)
    your_choices = [(u'produces', u'produces')]
    item_your = models.CharField(max_length=20, choices=your_choices, null=True)
    yourself_choices = [(u'produces', u'produces')]
    item_yourself = models.CharField(max_length=20, choices=yourself_choices, null=True)
    how_choices = [(u'produces', u'produces')]
    item_how = models.CharField(max_length=20, choices=how_choices, null=True)
    what_choices = [(u'produces', u'produces')]
    item_what = models.CharField(max_length=20, choices=what_choices, null=True)
    when_choices = [(u'produces', u'produces')]
    item_when = models.CharField(max_length=20, choices=when_choices, null=True)
    where_choices = [(u'produces', u'produces')]
    item_where = models.CharField(max_length=20, choices=where_choices, null=True)
    which_choices = [(u'produces', u'produces')]
    item_which = models.CharField(max_length=20, choices=which_choices, null=True)
    who_choices = [(u'produces', u'produces')]
    item_who = models.CharField(max_length=20, choices=who_choices, null=True)
    why_choices = [(u'produces', u'produces')]
    item_why = models.CharField(max_length=20, choices=why_choices, null=True)
    about_choices = [(u'produces', u'produces')]
    item_about = models.CharField(max_length=20, choices=about_choices, null=True)
    above_choices = [(u'produces', u'produces')]
    item_above = models.CharField(max_length=20, choices=above_choices, null=True)
    around_choices = [(u'produces', u'produces')]
    item_around = models.CharField(max_length=20, choices=around_choices, null=True)
    at_choices = [(u'produces', u'produces')]
    item_at = models.CharField(max_length=20, choices=at_choices, null=True)
    away_choices = [(u'produces', u'produces')]
    item_away = models.CharField(max_length=20, choices=away_choices, null=True)
    back_choices = [(u'produces', u'produces')]
    item_back = models.CharField(max_length=20, choices=back_choices, null=True)
    behind_choices = [(u'produces', u'produces')]
    item_behind = models.CharField(max_length=20, choices=behind_choices, null=True)
    beside_choices = [(u'produces', u'produces')]
    item_beside = models.CharField(max_length=20, choices=beside_choices, null=True)
    by_choices = [(u'produces', u'produces')]
    item_by = models.CharField(max_length=20, choices=by_choices, null=True)
    down_choices = [(u'produces', u'produces')]
    item_down = models.CharField(max_length=20, choices=down_choices, null=True)
    for_choices = [(u'produces', u'produces')]
    item_for = models.CharField(max_length=20, choices=for_choices, null=True)
    here_choices = [(u'produces', u'produces')]
    item_here = models.CharField(max_length=20, choices=here_choices, null=True)
    inside_choices = [(u'produces', u'produces')]
    item_inside = models.CharField(max_length=20, choices=inside_choices, null=True)
    into_choices = [(u'produces', u'produces')]
    item_into = models.CharField(max_length=20, choices=into_choices, null=True)
    next_to_choices = [(u'produces', u'produces')]
    item_next_to = models.CharField(max_length=20, choices=next_to_choices, null=True)
    of_choices = [(u'produces', u'produces')]
    item_of = models.CharField(max_length=20, choices=of_choices, null=True)
    off_choices = [(u'produces', u'produces')]
    item_off = models.CharField(max_length=20, choices=off_choices, null=True)
    on_choices = [(u'produces', u'produces')]
    item_on = models.CharField(max_length=20, choices=on_choices, null=True)
    on_top_of_choices = [(u'produces', u'produces')]
    item_on_top_of = models.CharField(max_length=20, choices=on_top_of_choices, null=True)
    out_choices = [(u'produces', u'produces')]
    item_out = models.CharField(max_length=20, choices=out_choices, null=True)
    over_choices = [(u'produces', u'produces')]
    item_over = models.CharField(max_length=20, choices=over_choices, null=True)
    there_choices = [(u'produces', u'produces')]
    item_there = models.CharField(max_length=20, choices=there_choices, null=True)
    to_choices = [(u'produces', u'produces')]
    item_to = models.CharField(max_length=20, choices=to_choices, null=True)
    under_choices = [(u'produces', u'produces')]
    item_under = models.CharField(max_length=20, choices=under_choices, null=True)
    up_choices = [(u'produces', u'produces')]
    item_up = models.CharField(max_length=20, choices=up_choices, null=True)
    with_choices = [(u'produces', u'produces')]
    item_with = models.CharField(max_length=20, choices=with_choices, null=True)
    a_choices = [(u'produces', u'produces')]
    item_a = models.CharField(max_length=20, choices=a_choices, null=True)
    all_choices = [(u'produces', u'produces')]
    item_all = models.CharField(max_length=20, choices=all_choices, null=True)
    a_lot_choices = [(u'produces', u'produces')]
    item_a_lot = models.CharField(max_length=20, choices=a_lot_choices, null=True)
    an_choices = [(u'produces', u'produces')]
    item_an = models.CharField(max_length=20, choices=an_choices, null=True)
    another_choices = [(u'produces', u'produces')]
    item_another = models.CharField(max_length=20, choices=another_choices, null=True)
    any_choices = [(u'produces', u'produces')]
    item_any = models.CharField(max_length=20, choices=any_choices, null=True)
    each_choices = [(u'produces', u'produces')]
    item_each = models.CharField(max_length=20, choices=each_choices, null=True)
    every_choices = [(u'produces', u'produces')]
    item_every = models.CharField(max_length=20, choices=every_choices, null=True)
    more_choices = [(u'produces', u'produces')]
    item_more = models.CharField(max_length=20, choices=more_choices, null=True)
    much_choices = [(u'produces', u'produces')]
    item_much = models.CharField(max_length=20, choices=much_choices, null=True)
    none_choices = [(u'produces', u'produces')]
    item_none = models.CharField(max_length=20, choices=none_choices, null=True)
    not_choices = [(u'produces', u'produces')]
    item_not = models.CharField(max_length=20, choices=not_choices, null=True)
    other_choices = [(u'produces', u'produces')]
    item_other = models.CharField(max_length=20, choices=other_choices, null=True)
    same_choices = [(u'produces', u'produces')]
    item_same = models.CharField(max_length=20, choices=same_choices, null=True)
    some_choices = [(u'produces', u'produces')]
    item_some = models.CharField(max_length=20, choices=some_choices, null=True)
    the_choices = [(u'produces', u'produces')]
    item_the = models.CharField(max_length=20, choices=the_choices, null=True)
    too_choices = [(u'produces', u'produces')]
    item_too = models.CharField(max_length=20, choices=too_choices, null=True)
    am_choices = [(u'produces', u'produces')]
    item_am = models.CharField(max_length=20, choices=am_choices, null=True)
    are_choices = [(u'produces', u'produces')]
    item_are = models.CharField(max_length=20, choices=are_choices, null=True)
    be_choices = [(u'produces', u'produces')]
    item_be = models.CharField(max_length=20, choices=be_choices, null=True)
    can_auxiliary_choices = [(u'produces', u'produces')]
    item_can_auxiliary = models.CharField(max_length=20, choices=can_auxiliary_choices, null=True)
    could_choices = [(u'produces', u'produces')]
    item_could = models.CharField(max_length=20, choices=could_choices, null=True)
    did_choices = [(u'produces', u'produces')]
    item_did = models.CharField(max_length=20, choices=did_choices, null=True)
    do_choices = [(u'produces', u'produces')]
    item_do = models.CharField(max_length=20, choices=do_choices, null=True)
    does_choices = [(u'produces', u'produces')]
    item_does = models.CharField(max_length=20, choices=does_choices, null=True)
    dont_choices = [(u'produces', u'produces')]
    item_dont = models.CharField(max_length=20, choices=dont_choices, null=True)
    gonna_choices = [(u'produces', u'produces')]
    item_gonna = models.CharField(max_length=20, choices=gonna_choices, null=True)
    gotta_choices = [(u'produces', u'produces')]
    item_gotta = models.CharField(max_length=20, choices=gotta_choices, null=True)
    hafta_choices = [(u'produces', u'produces')]
    item_hafta = models.CharField(max_length=20, choices=hafta_choices, null=True)
    is_choices = [(u'produces', u'produces')]
    item_is = models.CharField(max_length=20, choices=is_choices, null=True)
    lemme_choices = [(u'produces', u'produces')]
    item_lemme = models.CharField(max_length=20, choices=lemme_choices, null=True)
    need_choices = [(u'produces', u'produces')]
    item_need = models.CharField(max_length=20, choices=need_choices, null=True)
    try_choices = [(u'produces', u'produces')]
    item_try = models.CharField(max_length=20, choices=try_choices, null=True)
    wanna_choices = [(u'produces', u'produces')]
    item_wanna = models.CharField(max_length=20, choices=wanna_choices, null=True)
    was_choices = [(u'produces', u'produces')]
    item_was = models.CharField(max_length=20, choices=was_choices, null=True)
    were_choices = [(u'produces', u'produces')]
    item_were = models.CharField(max_length=20, choices=were_choices, null=True)
    will_choices = [(u'produces', u'produces')]
    item_will = models.CharField(max_length=20, choices=will_choices, null=True)
    would_choices = [(u'produces', u'produces')]
    item_would = models.CharField(max_length=20, choices=would_choices, null=True)
    and_choices = [(u'produces', u'produces')]
    item_and = models.CharField(max_length=20, choices=and_choices, null=True)
    because_choices = [(u'produces', u'produces')]
    item_because = models.CharField(max_length=20, choices=because_choices, null=True)
    but_choices = [(u'produces', u'produces')]
    item_but = models.CharField(max_length=20, choices=but_choices, null=True)
    if_choices = [(u'produces', u'produces')]
    item_if = models.CharField(max_length=20, choices=if_choices, null=True)
    so_choices = [(u'produces', u'produces')]
    item_so = models.CharField(max_length=20, choices=so_choices, null=True)
    then_choices = [(u'produces', u'produces')]
    item_then = models.CharField(max_length=20, choices=then_choices, null=True)
    usepast_choices = [(u'not yet', u'not yet'), (u'sometimes', u'sometimes'), (u'often', u'often')]
    item_usepast = models.CharField(max_length=20, choices=usepast_choices, null=True)
    usefuture_choices = [(u'not yet', u'not yet'), (u'sometimes', u'sometimes'), (u'often', u'often')]
    item_usefuture = models.CharField(max_length=20, choices=usefuture_choices, null=True)
    miss_produce_choices = [(u'not yet', u'not yet'), (u'sometimes', u'sometimes'), (u'often', u'often')]
    item_miss_produce = models.CharField(max_length=20, choices=miss_produce_choices, null=True)
    miss_comp_choices = [(u'not yet', u'not yet'), (u'sometimes', u'sometimes'), (u'often', u'often')]
    item_miss_comp = models.CharField(max_length=20, choices=miss_comp_choices, null=True)
    usepossessive_choices = [(u'not yet', u'not yet'), (u'sometimes', u'sometimes'), (u'often', u'often')]
    item_usepossessive = models.CharField(max_length=20, choices=usepossessive_choices, null=True)
    splural_choices = [(u'not yet', u'not yet'), (u'sometimes', u'sometimes'), (u'often', u'often')]
    item_splural = models.CharField(max_length=20, choices=splural_choices, null=True)
    spossess_choices = [(u'not yet', u'not yet'), (u'sometimes', u'sometimes'), (u'often', u'often')]
    item_spossess = models.CharField(max_length=20, choices=spossess_choices, null=True)
    ing_choices = [(u'not yet', u'not yet'), (u'sometimes', u'sometimes'), (u'often', u'often')]
    item_ing = models.CharField(max_length=20, choices=ing_choices, null=True)
    ed_choices = [(u'not yet', u'not yet'), (u'sometimes', u'sometimes'), (u'often', u'often')]
    item_ed = models.CharField(max_length=20, choices=ed_choices, null=True)
    children_choices = [(u'produces', u'produces')]
    item_children = models.CharField(max_length=20, choices=children_choices, null=True)
    feet_choices = [(u'produces', u'produces')]
    item_feet = models.CharField(max_length=20, choices=feet_choices, null=True)
    men_choices = [(u'produces', u'produces')]
    item_men = models.CharField(max_length=20, choices=men_choices, null=True)
    mice_choices = [(u'produces', u'produces')]
    item_mice = models.CharField(max_length=20, choices=mice_choices, null=True)
    teeth_choices = [(u'produces', u'produces')]
    item_teeth = models.CharField(max_length=20, choices=teeth_choices, null=True)
    ate_choices = [(u'produces', u'produces')]
    item_ate = models.CharField(max_length=20, choices=ate_choices, null=True)
    blew_choices = [(u'produces', u'produces')]
    item_blew = models.CharField(max_length=20, choices=blew_choices, null=True)
    bought_choices = [(u'produces', u'produces')]
    item_bought = models.CharField(max_length=20, choices=bought_choices, null=True)
    broke_choices = [(u'produces', u'produces')]
    item_broke = models.CharField(max_length=20, choices=broke_choices, null=True)
    came_choices = [(u'produces', u'produces')]
    item_came = models.CharField(max_length=20, choices=came_choices, null=True)
    drank_choices = [(u'produces', u'produces')]
    item_drank = models.CharField(max_length=20, choices=drank_choices, null=True)
    drove_choices = [(u'produces', u'produces')]
    item_drove = models.CharField(max_length=20, choices=drove_choices, null=True)
    fell_choices = [(u'produces', u'produces')]
    item_fell = models.CharField(max_length=20, choices=fell_choices, null=True)
    flew_choices = [(u'produces', u'produces')]
    item_flew = models.CharField(max_length=20, choices=flew_choices, null=True)
    got_choices = [(u'produces', u'produces')]
    item_got = models.CharField(max_length=20, choices=got_choices, null=True)
    had_choices = [(u'produces', u'produces')]
    item_had = models.CharField(max_length=20, choices=had_choices, null=True)
    heard_choices = [(u'produces', u'produces')]
    item_heard = models.CharField(max_length=20, choices=heard_choices, null=True)
    held_choices = [(u'produces', u'produces')]
    item_held = models.CharField(max_length=20, choices=held_choices, null=True)
    lost_choices = [(u'produces', u'produces')]
    item_lost = models.CharField(max_length=20, choices=lost_choices, null=True)
    made_choices = [(u'produces', u'produces')]
    item_made = models.CharField(max_length=20, choices=made_choices, null=True)
    ran_choices = [(u'produces', u'produces')]
    item_ran = models.CharField(max_length=20, choices=ran_choices, null=True)
    sat_choices = [(u'produces', u'produces')]
    item_sat = models.CharField(max_length=20, choices=sat_choices, null=True)
    saw_choices = [(u'produces', u'produces')]
    item_saw = models.CharField(max_length=20, choices=saw_choices, null=True)
    took_choices = [(u'produces', u'produces')]
    item_took = models.CharField(max_length=20, choices=took_choices, null=True)
    went_choices = [(u'produces', u'produces')]
    item_went = models.CharField(max_length=20, choices=went_choices, null=True)
    blockses_choices = [(u'produces', u'produces')]
    item_blockses = models.CharField(max_length=20, choices=blockses_choices, null=True)
    childrns_choices = [(u'produces', u'produces')]
    item_childrns = models.CharField(max_length=20, choices=childrns_choices, null=True)
    childs_choices = [(u'produces', u'produces')]
    item_childs = models.CharField(max_length=20, choices=childs_choices, null=True)
    feets_choices = [(u'produces', u'produces')]
    item_feets = models.CharField(max_length=20, choices=feets_choices, null=True)
    foots_choices = [(u'produces', u'produces')]
    item_foots = models.CharField(max_length=20, choices=foots_choices, null=True)
    mans_choices = [(u'produces', u'produces')]
    item_mans = models.CharField(max_length=20, choices=mans_choices, null=True)
    mens_choices = [(u'produces', u'produces')]
    item_mens = models.CharField(max_length=20, choices=mens_choices, null=True)
    mices_choices = [(u'produces', u'produces')]
    item_mices = models.CharField(max_length=20, choices=mices_choices, null=True)
    mouses_choices = [(u'produces', u'produces')]
    item_mouses = models.CharField(max_length=20, choices=mouses_choices, null=True)
    shoeses_choices = [(u'produces', u'produces')]
    item_shoeses = models.CharField(max_length=20, choices=shoeses_choices, null=True)
    sockses_choices = [(u'produces', u'produces')]
    item_sockses = models.CharField(max_length=20, choices=sockses_choices, null=True)
    teeths_choices = [(u'produces', u'produces')]
    item_teeths = models.CharField(max_length=20, choices=teeths_choices, null=True)
    toeses_choices = [(u'produces', u'produces')]
    item_toeses = models.CharField(max_length=20, choices=toeses_choices, null=True)
    tooths_choices = [(u'produces', u'produces')]
    item_tooths = models.CharField(max_length=20, choices=tooths_choices, null=True)
    ated_choices = [(u'produces', u'produces')]
    item_ated = models.CharField(max_length=20, choices=ated_choices, null=True)
    blewed_choices = [(u'produces', u'produces')]
    item_blewed = models.CharField(max_length=20, choices=blewed_choices, null=True)
    blowed_choices = [(u'produces', u'produces')]
    item_blowed = models.CharField(max_length=20, choices=blowed_choices, null=True)
    bringed_choices = [(u'produces', u'produces')]
    item_bringed = models.CharField(max_length=20, choices=bringed_choices, null=True)
    buyed_choices = [(u'produces', u'produces')]
    item_buyed = models.CharField(max_length=20, choices=buyed_choices, null=True)
    breaked_choices = [(u'produces', u'produces')]
    item_breaked = models.CharField(max_length=20, choices=breaked_choices, null=True)
    broked_choices = [(u'produces', u'produces')]
    item_broked = models.CharField(max_length=20, choices=broked_choices, null=True)
    camed_choices = [(u'produces', u'produces')]
    item_camed = models.CharField(max_length=20, choices=camed_choices, null=True)
    comed_choices = [(u'produces', u'produces')]
    item_comed = models.CharField(max_length=20, choices=comed_choices, null=True)
    doed_choices = [(u'produces', u'produces')]
    item_doed = models.CharField(max_length=20, choices=doed_choices, null=True)
    dranked_choices = [(u'produces', u'produces')]
    item_dranked = models.CharField(max_length=20, choices=dranked_choices, null=True)
    drinked_choices = [(u'produces', u'produces')]
    item_drinked = models.CharField(max_length=20, choices=drinked_choices, null=True)
    eated_choices = [(u'produces', u'produces')]
    item_eated = models.CharField(max_length=20, choices=eated_choices, null=True)
    falled_choices = [(u'produces', u'produces')]
    item_falled = models.CharField(max_length=20, choices=falled_choices, null=True)
    flied_choices = [(u'produces', u'produces')]
    item_flied = models.CharField(max_length=20, choices=flied_choices, null=True)
    getted_choices = [(u'produces', u'produces')]
    item_getted = models.CharField(max_length=20, choices=getted_choices, null=True)
    goed_choices = [(u'produces', u'produces')]
    item_goed = models.CharField(max_length=20, choices=goed_choices, null=True)
    gotted_choices = [(u'produces', u'produces')]
    item_gotted = models.CharField(max_length=20, choices=gotted_choices, null=True)
    haved_choices = [(u'produces', u'produces')]
    item_haved = models.CharField(max_length=20, choices=haved_choices, null=True)
    heared_choices = [(u'produces', u'produces')]
    item_heared = models.CharField(max_length=20, choices=heared_choices, null=True)
    holded_choices = [(u'produces', u'produces')]
    item_holded = models.CharField(max_length=20, choices=holded_choices, null=True)
    losed_choices = [(u'produces', u'produces')]
    item_losed = models.CharField(max_length=20, choices=losed_choices, null=True)
    losted_choices = [(u'produces', u'produces')]
    item_losted = models.CharField(max_length=20, choices=losted_choices, null=True)
    maked_choices = [(u'produces', u'produces')]
    item_maked = models.CharField(max_length=20, choices=maked_choices, null=True)
    ranned_choices = [(u'produces', u'produces')]
    item_ranned = models.CharField(max_length=20, choices=ranned_choices, null=True)
    runned_choices = [(u'produces', u'produces')]
    item_runned = models.CharField(max_length=20, choices=runned_choices, null=True)
    seed_choices = [(u'produces', u'produces')]
    item_seed = models.CharField(max_length=20, choices=seed_choices, null=True)
    satted_choices = [(u'produces', u'produces')]
    item_satted = models.CharField(max_length=20, choices=satted_choices, null=True)
    sitted_choices = [(u'produces', u'produces')]
    item_sitted = models.CharField(max_length=20, choices=sitted_choices, null=True)
    taked_choices = [(u'produces', u'produces')]
    item_taked = models.CharField(max_length=20, choices=taked_choices, null=True)
    wented_choices = [(u'produces', u'produces')]
    item_wented = models.CharField(max_length=20, choices=wented_choices, null=True)
    combine_choices = [(u'not yet', u'not yet'), (u'sometimes', u'sometimes'), (u'often', u'often')]
    item_combine = models.CharField(max_length=20, choices=combine_choices, null=True)
    complx01_choices = [(u'simple', u'simple'), (u'complex', u'complex')]
    item_complx01 = models.CharField(max_length=20, choices=complx01_choices, null=True)
    complx02_choices = [(u'simple', u'simple'), (u'complex', u'complex')]
    item_complx02 = models.CharField(max_length=20, choices=complx02_choices, null=True)
    complx03_choices = [(u'simple', u'simple'), (u'complex', u'complex')]
    item_complx03 = models.CharField(max_length=20, choices=complx03_choices, null=True)
    complx04_choices = [(u'simple', u'simple'), (u'complex', u'complex')]
    item_complx04 = models.CharField(max_length=20, choices=complx04_choices, null=True)
    complx05_choices = [(u'simple', u'simple'), (u'complex', u'complex')]
    item_complx05 = models.CharField(max_length=20, choices=complx05_choices, null=True)
    complx06_choices = [(u'simple', u'simple'), (u'complex', u'complex')]
    item_complx06 = models.CharField(max_length=20, choices=complx06_choices, null=True)
    complx07_choices = [(u'simple', u'simple'), (u'complex', u'complex')]
    item_complx07 = models.CharField(max_length=20, choices=complx07_choices, null=True)
    complx08_choices = [(u'simple', u'simple'), (u'complex', u'complex')]
    item_complx08 = models.CharField(max_length=20, choices=complx08_choices, null=True)
    complx09_choices = [(u'simple', u'simple'), (u'complex', u'complex')]
    item_complx09 = models.CharField(max_length=20, choices=complx09_choices, null=True)
    complx10_choices = [(u'simple', u'simple'), (u'complex', u'complex')]
    item_complx10 = models.CharField(max_length=20, choices=complx10_choices, null=True)
    complx11_choices = [(u'simple', u'simple'), (u'complex', u'complex')]
    item_complx11 = models.CharField(max_length=20, choices=complx11_choices, null=True)
    complx12_choices = [(u'simple', u'simple'), (u'complex', u'complex')]
    item_complx12 = models.CharField(max_length=20, choices=complx12_choices, null=True)
    complx13_choices = [(u'simple', u'simple'), (u'complex', u'complex')]
    item_complx13 = models.CharField(max_length=20, choices=complx13_choices, null=True)
    complx14_choices = [(u'simple', u'simple'), (u'complex', u'complex')]
    item_complx14 = models.CharField(max_length=20, choices=complx14_choices, null=True)
    complx15_choices = [(u'simple', u'simple'), (u'complex', u'complex')]
    item_complx15 = models.CharField(max_length=20, choices=complx15_choices, null=True)
    complx16_choices = [(u'simple', u'simple'), (u'complex', u'complex')]
    item_complx16 = models.CharField(max_length=20, choices=complx16_choices, null=True)
    complx17_choices = [(u'simple', u'simple'), (u'complex', u'complex')]
    item_complx17 = models.CharField(max_length=20, choices=complx17_choices, null=True)
    complx18_choices = [(u'simple', u'simple'), (u'complex', u'complex')]
    item_complx18 = models.CharField(max_length=20, choices=complx18_choices, null=True)
    complx19_choices = [(u'simple', u'simple'), (u'complex', u'complex')]
    item_complx19 = models.CharField(max_length=20, choices=complx19_choices, null=True)
    complx20_choices = [(u'simple', u'simple'), (u'complex', u'complex')]
    item_complx20 = models.CharField(max_length=20, choices=complx20_choices, null=True)
    complx21_choices = [(u'simple', u'simple'), (u'complex', u'complex')]
    item_complx21 = models.CharField(max_length=20, choices=complx21_choices, null=True)
    complx22_choices = [(u'simple', u'simple'), (u'complex', u'complex')]
    item_complx22 = models.CharField(max_length=20, choices=complx22_choices, null=True)
    complx23_choices = [(u'simple', u'simple'), (u'complex', u'complex')]
    item_complx23 = models.CharField(max_length=20, choices=complx23_choices, null=True)
    complx24_choices = [(u'simple', u'simple'), (u'complex', u'complex')]
    item_complx24 = models.CharField(max_length=20, choices=complx24_choices, null=True)
    complx25_choices = [(u'simple', u'simple'), (u'complex', u'complex')]
    item_complx25 = models.CharField(max_length=20, choices=complx25_choices, null=True)
    complx26_choices = [(u'simple', u'simple'), (u'complex', u'complex')]
    item_complx26 = models.CharField(max_length=20, choices=complx26_choices, null=True)
    complx27_choices = [(u'simple', u'simple'), (u'complex', u'complex')]
    item_complx27 = models.CharField(max_length=20, choices=complx27_choices, null=True)
    complx28_choices = [(u'simple', u'simple'), (u'complex', u'complex')]
    item_complx28 = models.CharField(max_length=20, choices=complx28_choices, null=True)
    complx29_choices = [(u'simple', u'simple'), (u'complex', u'complex')]
    item_complx29 = models.CharField(max_length=20, choices=complx29_choices, null=True)
    complx30_choices = [(u'simple', u'simple'), (u'complex', u'complex')]
    item_complx30 = models.CharField(max_length=20, choices=complx30_choices, null=True)
    complx31_choices = [(u'simple', u'simple'), (u'complex', u'complex')]
    item_complx31 = models.CharField(max_length=20, choices=complx31_choices, null=True)
    complx32_choices = [(u'simple', u'simple'), (u'complex', u'complex')]
    item_complx32 = models.CharField(max_length=20, choices=complx32_choices, null=True)
    complx33_choices = [(u'simple', u'simple'), (u'complex', u'complex')]
    item_complx33 = models.CharField(max_length=20, choices=complx33_choices, null=True)
    complx34_choices = [(u'simple', u'simple'), (u'complex', u'complex')]
    item_complx34 = models.CharField(max_length=20, choices=complx34_choices, null=True)
    complx35_choices = [(u'simple', u'simple'), (u'complex', u'complex')]
    item_complx35 = models.CharField(max_length=20, choices=complx35_choices, null=True)
    complx36_choices = [(u'simple', u'simple'), (u'complex', u'complex')]
    item_complx36 = models.CharField(max_length=20, choices=complx36_choices, null=True)
    complx37_choices = [(u'simple', u'simple'), (u'complex', u'complex')]
    item_complx37 = models.CharField(max_length=20, choices=complx37_choices, null=True)


class English_WG(BaseTable):
    respname_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_respname = models.CharField(max_length=20, choices=respname_choices, null=True)
    respno_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_respno = models.CharField(max_length=20, choices=respno_choices, null=True)
    reactmd_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_reactmd = models.CharField(max_length=20, choices=reactmd_choices, null=True)
    arehngry_choices = [(u'understands', u'understands')]
    item_arehngry = models.CharField(max_length=20, choices=arehngry_choices, null=True)
    aretired_choices = [(u'understands', u'understands')]
    item_aretired = models.CharField(max_length=20, choices=aretired_choices, null=True)
    becarefl_choices = [(u'understands', u'understands')]
    item_becarefl = models.CharField(max_length=20, choices=becarefl_choices, null=True)
    bequiet_choices = [(u'understands', u'understands')]
    item_bequiet = models.CharField(max_length=20, choices=bequiet_choices, null=True)
    claphand_choices = [(u'understands', u'understands')]
    item_claphand = models.CharField(max_length=20, choices=claphand_choices, null=True)
    cgdiaper_choices = [(u'understands', u'understands')]
    item_cgdiaper = models.CharField(max_length=20, choices=cgdiaper_choices, null=True)
    comehere_choices = [(u'understands', u'understands')]
    item_comehere = models.CharField(max_length=20, choices=comehere_choices, null=True)
    mdhome_choices = [(u'understands', u'understands')]
    item_mdhome = models.CharField(max_length=20, choices=mdhome_choices, null=True)
    wantmore_choices = [(u'understands', u'understands')]
    item_wantmore = models.CharField(max_length=20, choices=wantmore_choices, null=True)
    dontdo_choices = [(u'understands', u'understands')]
    item_dontdo = models.CharField(max_length=20, choices=dontdo_choices, null=True)
    dontouch_choices = [(u'understands', u'understands')]
    item_dontouch = models.CharField(max_length=20, choices=dontouch_choices, null=True)
    getup_choices = [(u'understands', u'understands')]
    item_getup = models.CharField(max_length=20, choices=getup_choices, null=True)
    givemom_choices = [(u'understands', u'understands')]
    item_givemom = models.CharField(max_length=20, choices=givemom_choices, null=True)
    givehug_choices = [(u'understands', u'understands')]
    item_givehug = models.CharField(max_length=20, choices=givehug_choices, null=True)
    givekiss_choices = [(u'understands', u'understands')]
    item_givekiss = models.CharField(max_length=20, choices=givekiss_choices, null=True)
    goget_choices = [(u'understands', u'understands')]
    item_goget = models.CharField(max_length=20, choices=goget_choices, null=True)
    goodgb_choices = [(u'understands', u'understands')]
    item_goodgb = models.CharField(max_length=20, choices=goodgb_choices, null=True)
    holdstil_choices = [(u'understands', u'understands')]
    item_holdstil = models.CharField(max_length=20, choices=holdstil_choices, null=True)
    gobyebye_choices = [(u'understands', u'understands')]
    item_gobyebye = models.CharField(max_length=20, choices=gobyebye_choices, null=True)
    lookhere_choices = [(u'understands', u'understands')]
    item_lookhere = models.CharField(max_length=20, choices=lookhere_choices, null=True)
    openmth_choices = [(u'understands', u'understands')]
    item_openmth = models.CharField(max_length=20, choices=openmth_choices, null=True)
    sitdown_choices = [(u'understands', u'understands')]
    item_sitdown = models.CharField(max_length=20, choices=sitdown_choices, null=True)
    spitout_choices = [(u'understands', u'understands')]
    item_spitout = models.CharField(max_length=20, choices=spitout_choices, null=True)
    stopit_choices = [(u'understands', u'understands')]
    item_stopit = models.CharField(max_length=20, choices=stopit_choices, null=True)
    gonight_choices = [(u'understands', u'understands')]
    item_gonight = models.CharField(max_length=20, choices=gonight_choices, null=True)
    throwbll_choices = [(u'understands', u'understands')]
    item_throwbll = models.CharField(max_length=20, choices=throwbll_choices, null=True)
    litpiggy_choices = [(u'understands', u'understands')]
    item_litpiggy = models.CharField(max_length=20, choices=litpiggy_choices, null=True)
    wantride_choices = [(u'understands', u'understands')]
    item_wantride = models.CharField(max_length=20, choices=wantride_choices, null=True)
    imitate_choices = [(u'never', u'never'), (u'sometimes', u'sometimes'), (u'often', u'often')]
    item_imitate = models.CharField(max_length=20, choices=imitate_choices, null=True)
    label_choices = [(u'never', u'never'), (u'sometimes', u'sometimes'), (u'often', u'often')]
    item_label = models.CharField(max_length=20, choices=label_choices, null=True)
    baa_baa_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_baa_baa = models.CharField(max_length=20, choices=baa_baa_choices, null=True)
    choo_choo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_choo_choo = models.CharField(max_length=20, choices=choo_choo_choices, null=True)
    cockadoodledoo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cockadoodledoo = models.CharField(max_length=20, choices=cockadoodledoo_choices, null=True)
    grrr_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_grrr = models.CharField(max_length=20, choices=grrr_choices, null=True)
    meow_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_meow = models.CharField(max_length=20, choices=meow_choices, null=True)
    moo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_moo = models.CharField(max_length=20, choices=moo_choices, null=True)
    ouch_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_ouch = models.CharField(max_length=20, choices=ouch_choices, null=True)
    quack_quack_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_quack_quack = models.CharField(max_length=20, choices=quack_quack_choices, null=True)
    uh_oh_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_uh_oh = models.CharField(max_length=20, choices=uh_oh_choices, null=True)
    vroom_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_vroom = models.CharField(max_length=20, choices=vroom_choices, null=True)
    woof_woof_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_woof_woof = models.CharField(max_length=20, choices=woof_woof_choices, null=True)
    yum_yum_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_yum_yum = models.CharField(max_length=20, choices=yum_yum_choices, null=True)
    animal_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_animal = models.CharField(max_length=20, choices=animal_choices, null=True)
    bear_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_bear = models.CharField(max_length=20, choices=bear_choices, null=True)
    bee_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_bee = models.CharField(max_length=20, choices=bee_choices, null=True)
    bird_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_bird = models.CharField(max_length=20, choices=bird_choices, null=True)
    bug_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_bug = models.CharField(max_length=20, choices=bug_choices, null=True)
    bunny_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_bunny = models.CharField(max_length=20, choices=bunny_choices, null=True)
    butterfly_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_butterfly = models.CharField(max_length=20, choices=butterfly_choices, null=True)
    cat_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cat = models.CharField(max_length=20, choices=cat_choices, null=True)
    chicken_animal_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_chicken_animal = models.CharField(max_length=20, choices=chicken_animal_choices, null=True)
    cow_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cow = models.CharField(max_length=20, choices=cow_choices, null=True)
    deer_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_deer = models.CharField(max_length=20, choices=deer_choices, null=True)
    dog_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_dog = models.CharField(max_length=20, choices=dog_choices, null=True)
    donkey_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_donkey = models.CharField(max_length=20, choices=donkey_choices, null=True)
    duck_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_duck = models.CharField(max_length=20, choices=duck_choices, null=True)
    elephant_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_elephant = models.CharField(max_length=20, choices=elephant_choices, null=True)
    fish_animal_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_fish_animal = models.CharField(max_length=20, choices=fish_animal_choices, null=True)
    frog_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_frog = models.CharField(max_length=20, choices=frog_choices, null=True)
    giraffe_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_giraffe = models.CharField(max_length=20, choices=giraffe_choices, null=True)
    goose_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_goose = models.CharField(max_length=20, choices=goose_choices, null=True)
    horse_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_horse = models.CharField(max_length=20, choices=horse_choices, null=True)
    kitty_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_kitty = models.CharField(max_length=20, choices=kitty_choices, null=True)
    lamb_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_lamb = models.CharField(max_length=20, choices=lamb_choices, null=True)
    lion_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_lion = models.CharField(max_length=20, choices=lion_choices, null=True)
    monkey_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_monkey = models.CharField(max_length=20, choices=monkey_choices, null=True)
    mouse_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_mouse = models.CharField(max_length=20, choices=mouse_choices, null=True)
    owl_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_owl = models.CharField(max_length=20, choices=owl_choices, null=True)
    penguin_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_penguin = models.CharField(max_length=20, choices=penguin_choices, null=True)
    pig_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_pig = models.CharField(max_length=20, choices=pig_choices, null=True)
    pony_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_pony = models.CharField(max_length=20, choices=pony_choices, null=True)
    puppy_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_puppy = models.CharField(max_length=20, choices=puppy_choices, null=True)
    sheep_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_sheep = models.CharField(max_length=20, choices=sheep_choices, null=True)
    squirrel_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_squirrel = models.CharField(max_length=20, choices=squirrel_choices, null=True)
    teddybear_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_teddybear = models.CharField(max_length=20, choices=teddybear_choices, null=True)
    tiger_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_tiger = models.CharField(max_length=20, choices=tiger_choices, null=True)
    turkey_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_turkey = models.CharField(max_length=20, choices=turkey_choices, null=True)
    turtle_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_turtle = models.CharField(max_length=20, choices=turtle_choices, null=True)
    airplane_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_airplane = models.CharField(max_length=20, choices=airplane_choices, null=True)
    bicycle_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_bicycle = models.CharField(max_length=20, choices=bicycle_choices, null=True)
    bus_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_bus = models.CharField(max_length=20, choices=bus_choices, null=True)
    car_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_car = models.CharField(max_length=20, choices=car_choices, null=True)
    firetruck_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_firetruck = models.CharField(max_length=20, choices=firetruck_choices, null=True)
    motorcycle_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_motorcycle = models.CharField(max_length=20, choices=motorcycle_choices, null=True)
    stroller_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_stroller = models.CharField(max_length=20, choices=stroller_choices, null=True)
    train_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_train = models.CharField(max_length=20, choices=train_choices, null=True)
    truck_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_truck = models.CharField(max_length=20, choices=truck_choices, null=True)
    ball_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_ball = models.CharField(max_length=20, choices=ball_choices, null=True)
    balloon_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_balloon = models.CharField(max_length=20, choices=balloon_choices, null=True)
    block_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_block = models.CharField(max_length=20, choices=block_choices, null=True)
    book_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_book = models.CharField(max_length=20, choices=book_choices, null=True)
    bubbles_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_bubbles = models.CharField(max_length=20, choices=bubbles_choices, null=True)
    doll_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_doll = models.CharField(max_length=20, choices=doll_choices, null=True)
    pen_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_pen = models.CharField(max_length=20, choices=pen_choices, null=True)
    toy_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_toy = models.CharField(max_length=20, choices=toy_choices, null=True)
    apple_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_apple = models.CharField(max_length=20, choices=apple_choices, null=True)
    banana_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_banana = models.CharField(max_length=20, choices=banana_choices, null=True)
    bread_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_bread = models.CharField(max_length=20, choices=bread_choices, null=True)
    butter_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_butter = models.CharField(max_length=20, choices=butter_choices, null=True)
    cake_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cake = models.CharField(max_length=20, choices=cake_choices, null=True)
    candy_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_candy = models.CharField(max_length=20, choices=candy_choices, null=True)
    carrots_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_carrots = models.CharField(max_length=20, choices=carrots_choices, null=True)
    cereal_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cereal = models.CharField(max_length=20, choices=cereal_choices, null=True)
    cheerios_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cheerios = models.CharField(max_length=20, choices=cheerios_choices, null=True)
    cheese_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cheese = models.CharField(max_length=20, choices=cheese_choices, null=True)
    chicken_food_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_chicken_food = models.CharField(max_length=20, choices=chicken_food_choices, null=True)
    coffee_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_coffee = models.CharField(max_length=20, choices=coffee_choices, null=True)
    cookie_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cookie = models.CharField(max_length=20, choices=cookie_choices, null=True)
    cracker_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cracker = models.CharField(max_length=20, choices=cracker_choices, null=True)
    drink_beverage_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_drink_beverage = models.CharField(max_length=20, choices=drink_beverage_choices, null=True)
    egg_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_egg = models.CharField(max_length=20, choices=egg_choices, null=True)
    fish_food_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_fish_food = models.CharField(max_length=20, choices=fish_food_choices, null=True)
    food_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_food = models.CharField(max_length=20, choices=food_choices, null=True)
    ice_cream_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_ice_cream = models.CharField(max_length=20, choices=ice_cream_choices, null=True)
    juice_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_juice = models.CharField(max_length=20, choices=juice_choices, null=True)
    meat_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_meat = models.CharField(max_length=20, choices=meat_choices, null=True)
    milk_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_milk = models.CharField(max_length=20, choices=milk_choices, null=True)
    noodles_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_noodles = models.CharField(max_length=20, choices=noodles_choices, null=True)
    orange_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_orange = models.CharField(max_length=20, choices=orange_choices, null=True)
    peas_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_peas = models.CharField(max_length=20, choices=peas_choices, null=True)
    pizza_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_pizza = models.CharField(max_length=20, choices=pizza_choices, null=True)
    raisin_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_raisin = models.CharField(max_length=20, choices=raisin_choices, null=True)
    spaghetti_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_spaghetti = models.CharField(max_length=20, choices=spaghetti_choices, null=True)
    toast_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_toast = models.CharField(max_length=20, choices=toast_choices, null=True)
    water_beverage_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_water_beverage = models.CharField(max_length=20, choices=water_beverage_choices, null=True)
    beads_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_beads = models.CharField(max_length=20, choices=beads_choices, null=True)
    bib_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_bib = models.CharField(max_length=20, choices=bib_choices, null=True)
    boots_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_boots = models.CharField(max_length=20, choices=boots_choices, null=True)
    button_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_button = models.CharField(max_length=20, choices=button_choices, null=True)
    coat_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_coat = models.CharField(max_length=20, choices=coat_choices, null=True)
    diaper_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_diaper = models.CharField(max_length=20, choices=diaper_choices, null=True)
    dress_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_dress = models.CharField(max_length=20, choices=dress_choices, null=True)
    hat_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_hat = models.CharField(max_length=20, choices=hat_choices, null=True)
    jacket_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_jacket = models.CharField(max_length=20, choices=jacket_choices, null=True)
    jeans_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_jeans = models.CharField(max_length=20, choices=jeans_choices, null=True)
    necklace_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_necklace = models.CharField(max_length=20, choices=necklace_choices, null=True)
    pajamas_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_pajamas = models.CharField(max_length=20, choices=pajamas_choices, null=True)
    pants_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_pants = models.CharField(max_length=20, choices=pants_choices, null=True)
    shirt_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_shirt = models.CharField(max_length=20, choices=shirt_choices, null=True)
    shoe_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_shoe = models.CharField(max_length=20, choices=shoe_choices, null=True)
    shorts_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_shorts = models.CharField(max_length=20, choices=shorts_choices, null=True)
    sock_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_sock = models.CharField(max_length=20, choices=sock_choices, null=True)
    sweater_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_sweater = models.CharField(max_length=20, choices=sweater_choices, null=True)
    zipper_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_zipper = models.CharField(max_length=20, choices=zipper_choices, null=True)
    arm_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_arm = models.CharField(max_length=20, choices=arm_choices, null=True)
    belly_button_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_belly_button = models.CharField(max_length=20, choices=belly_button_choices, null=True)
    cheek_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cheek = models.CharField(max_length=20, choices=cheek_choices, null=True)
    ear_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_ear = models.CharField(max_length=20, choices=ear_choices, null=True)
    eye_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_eye = models.CharField(max_length=20, choices=eye_choices, null=True)
    face_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_face = models.CharField(max_length=20, choices=face_choices, null=True)
    foot_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_foot = models.CharField(max_length=20, choices=foot_choices, null=True)
    finger_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_finger = models.CharField(max_length=20, choices=finger_choices, null=True)
    hair_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_hair = models.CharField(max_length=20, choices=hair_choices, null=True)
    hand_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_hand = models.CharField(max_length=20, choices=hand_choices, null=True)
    head_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_head = models.CharField(max_length=20, choices=head_choices, null=True)
    knee_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_knee = models.CharField(max_length=20, choices=knee_choices, null=True)
    leg_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_leg = models.CharField(max_length=20, choices=leg_choices, null=True)
    mouth_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_mouth = models.CharField(max_length=20, choices=mouth_choices, null=True)
    nose_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_nose = models.CharField(max_length=20, choices=nose_choices, null=True)
    owie_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_owie = models.CharField(max_length=20, choices=owie_choices, null=True)
    tooth_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_tooth = models.CharField(max_length=20, choices=tooth_choices, null=True)
    toe_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_toe = models.CharField(max_length=20, choices=toe_choices, null=True)
    tongue_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_tongue = models.CharField(max_length=20, choices=tongue_choices, null=True)
    tummy_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_tummy = models.CharField(max_length=20, choices=tummy_choices, null=True)
    bathroom_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_bathroom = models.CharField(max_length=20, choices=bathroom_choices, null=True)
    bathtub_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_bathtub = models.CharField(max_length=20, choices=bathtub_choices, null=True)
    bed_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_bed = models.CharField(max_length=20, choices=bed_choices, null=True)
    bedroom_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_bedroom = models.CharField(max_length=20, choices=bedroom_choices, null=True)
    chair_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_chair = models.CharField(max_length=20, choices=chair_choices, null=True)
    couch_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_couch = models.CharField(max_length=20, choices=couch_choices, null=True)
    crib_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_crib = models.CharField(max_length=20, choices=crib_choices, null=True)
    door_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_door = models.CharField(max_length=20, choices=door_choices, null=True)
    drawer_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_drawer = models.CharField(max_length=20, choices=drawer_choices, null=True)
    garage_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_garage = models.CharField(max_length=20, choices=garage_choices, null=True)
    high_chair_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_high_chair = models.CharField(max_length=20, choices=high_chair_choices, null=True)
    kitchen_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_kitchen = models.CharField(max_length=20, choices=kitchen_choices, null=True)
    living_room_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_living_room = models.CharField(max_length=20, choices=living_room_choices, null=True)
    oven_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_oven = models.CharField(max_length=20, choices=oven_choices, null=True)
    play_pen_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_play_pen = models.CharField(max_length=20, choices=play_pen_choices, null=True)
    potty_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_potty = models.CharField(max_length=20, choices=potty_choices, null=True)
    refrigerator_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_refrigerator = models.CharField(max_length=20, choices=refrigerator_choices, null=True)
    rocking_chair_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_rocking_chair = models.CharField(max_length=20, choices=rocking_chair_choices, null=True)
    sink_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_sink = models.CharField(max_length=20, choices=sink_choices, null=True)
    stairs_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_stairs = models.CharField(max_length=20, choices=stairs_choices, null=True)
    stove_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_stove = models.CharField(max_length=20, choices=stove_choices, null=True)
    table_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_table = models.CharField(max_length=20, choices=table_choices, null=True)
    tv_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_tv = models.CharField(max_length=20, choices=tv_choices, null=True)
    window_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_window = models.CharField(max_length=20, choices=window_choices, null=True)
    blanket_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_blanket = models.CharField(max_length=20, choices=blanket_choices, null=True)
    bottle_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_bottle = models.CharField(max_length=20, choices=bottle_choices, null=True)
    bowl_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_bowl = models.CharField(max_length=20, choices=bowl_choices, null=True)
    box_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_box = models.CharField(max_length=20, choices=box_choices, null=True)
    broom_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_broom = models.CharField(max_length=20, choices=broom_choices, null=True)
    brush_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_brush = models.CharField(max_length=20, choices=brush_choices, null=True)
    clock_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_clock = models.CharField(max_length=20, choices=clock_choices, null=True)
    comb_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_comb = models.CharField(max_length=20, choices=comb_choices, null=True)
    cup_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cup = models.CharField(max_length=20, choices=cup_choices, null=True)
    dish_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_dish = models.CharField(max_length=20, choices=dish_choices, null=True)
    fork_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_fork = models.CharField(max_length=20, choices=fork_choices, null=True)
    glass_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_glass = models.CharField(max_length=20, choices=glass_choices, null=True)
    glasses_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_glasses = models.CharField(max_length=20, choices=glasses_choices, null=True)
    hammer_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_hammer = models.CharField(max_length=20, choices=hammer_choices, null=True)
    keys_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_keys = models.CharField(max_length=20, choices=keys_choices, null=True)
    lamp_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_lamp = models.CharField(max_length=20, choices=lamp_choices, null=True)
    light_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_light = models.CharField(max_length=20, choices=light_choices, null=True)
    medicine_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_medicine = models.CharField(max_length=20, choices=medicine_choices, null=True)
    money_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_money = models.CharField(max_length=20, choices=money_choices, null=True)
    paper_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_paper = models.CharField(max_length=20, choices=paper_choices, null=True)
    penny_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_penny = models.CharField(max_length=20, choices=penny_choices, null=True)
    picture_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_picture = models.CharField(max_length=20, choices=picture_choices, null=True)
    pillow_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_pillow = models.CharField(max_length=20, choices=pillow_choices, null=True)
    plant_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_plant = models.CharField(max_length=20, choices=plant_choices, null=True)
    plate_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_plate = models.CharField(max_length=20, choices=plate_choices, null=True)
    purse_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_purse = models.CharField(max_length=20, choices=purse_choices, null=True)
    radio_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_radio = models.CharField(max_length=20, choices=radio_choices, null=True)
    scissors_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_scissors = models.CharField(max_length=20, choices=scissors_choices, null=True)
    soap_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_soap = models.CharField(max_length=20, choices=soap_choices, null=True)
    spoon_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_spoon = models.CharField(max_length=20, choices=spoon_choices, null=True)
    telephone_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_telephone = models.CharField(max_length=20, choices=telephone_choices, null=True)
    toothbrush_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_toothbrush = models.CharField(max_length=20, choices=toothbrush_choices, null=True)
    towel_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_towel = models.CharField(max_length=20, choices=towel_choices, null=True)
    trash_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_trash = models.CharField(max_length=20, choices=trash_choices, null=True)
    vacuum_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_vacuum = models.CharField(max_length=20, choices=vacuum_choices, null=True)
    watch_object_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_watch_object = models.CharField(max_length=20, choices=watch_object_choices, null=True)
    backyard_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_backyard = models.CharField(max_length=20, choices=backyard_choices, null=True)
    beach_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_beach = models.CharField(max_length=20, choices=beach_choices, null=True)
    church_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_church = models.CharField(max_length=20, choices=church_choices, null=True)
    flower_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_flower = models.CharField(max_length=20, choices=flower_choices, null=True)
    garden_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_garden = models.CharField(max_length=20, choices=garden_choices, null=True)
    home_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_home = models.CharField(max_length=20, choices=home_choices, null=True)
    house_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_house = models.CharField(max_length=20, choices=house_choices, null=True)
    moon_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_moon = models.CharField(max_length=20, choices=moon_choices, null=True)
    outside_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_outside = models.CharField(max_length=20, choices=outside_choices, null=True)
    park_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_park = models.CharField(max_length=20, choices=park_choices, null=True)
    party_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_party = models.CharField(max_length=20, choices=party_choices, null=True)
    pool_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_pool = models.CharField(max_length=20, choices=pool_choices, null=True)
    rain_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_rain = models.CharField(max_length=20, choices=rain_choices, null=True)
    rock_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_rock = models.CharField(max_length=20, choices=rock_choices, null=True)
    school_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_school = models.CharField(max_length=20, choices=school_choices, null=True)
    shovel_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_shovel = models.CharField(max_length=20, choices=shovel_choices, null=True)
    sky_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_sky = models.CharField(max_length=20, choices=sky_choices, null=True)
    slide_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_slide = models.CharField(max_length=20, choices=slide_choices, null=True)
    snow_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_snow = models.CharField(max_length=20, choices=snow_choices, null=True)
    star_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_star = models.CharField(max_length=20, choices=star_choices, null=True)
    store_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_store = models.CharField(max_length=20, choices=store_choices, null=True)
    sun_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_sun = models.CharField(max_length=20, choices=sun_choices, null=True)
    swing_object_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_swing_object = models.CharField(max_length=20, choices=swing_object_choices, null=True)
    tree_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_tree = models.CharField(max_length=20, choices=tree_choices, null=True)
    water_not_beverage_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_water_not_beverage = models.CharField(max_length=20, choices=water_not_beverage_choices, null=True)
    work_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_work = models.CharField(max_length=20, choices=work_choices, null=True)
    zoo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_zoo = models.CharField(max_length=20, choices=zoo_choices, null=True)
    aunt_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_aunt = models.CharField(max_length=20, choices=aunt_choices, null=True)
    baby_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_baby = models.CharField(max_length=20, choices=baby_choices, null=True)
    babysitter_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_babysitter = models.CharField(max_length=20, choices=babysitter_choices, null=True)
    babysitter_name_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_babysitter_name = models.CharField(max_length=20, choices=babysitter_name_choices, null=True)
    boy_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_boy = models.CharField(max_length=20, choices=boy_choices, null=True)
    brother_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_brother = models.CharField(max_length=20, choices=brother_choices, null=True)
    child_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_child = models.CharField(max_length=20, choices=child_choices, null=True)
    daddy_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_daddy = models.CharField(max_length=20, choices=daddy_choices, null=True)
    girl_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_girl = models.CharField(max_length=20, choices=girl_choices, null=True)
    grandma_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_grandma = models.CharField(max_length=20, choices=grandma_choices, null=True)
    grandpa_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_grandpa = models.CharField(max_length=20, choices=grandpa_choices, null=True)
    lady_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_lady = models.CharField(max_length=20, choices=lady_choices, null=True)
    man_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_man = models.CharField(max_length=20, choices=man_choices, null=True)
    mommy_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_mommy = models.CharField(max_length=20, choices=mommy_choices, null=True)
    child_own_name_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_child_own_name = models.CharField(max_length=20, choices=child_own_name_choices, null=True)
    people_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_people = models.CharField(max_length=20, choices=people_choices, null=True)
    person_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_person = models.CharField(max_length=20, choices=person_choices, null=True)
    sister_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_sister = models.CharField(max_length=20, choices=sister_choices, null=True)
    teacher_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_teacher = models.CharField(max_length=20, choices=teacher_choices, null=True)
    uncle_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_uncle = models.CharField(max_length=20, choices=uncle_choices, null=True)
    bath_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_bath = models.CharField(max_length=20, choices=bath_choices, null=True)
    breakfast_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_breakfast = models.CharField(max_length=20, choices=breakfast_choices, null=True)
    bye_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_bye = models.CharField(max_length=20, choices=bye_choices, null=True)
    dinner_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_dinner = models.CharField(max_length=20, choices=dinner_choices, null=True)
    dont_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_dont = models.CharField(max_length=20, choices=dont_choices, null=True)
    hello_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_hello = models.CharField(max_length=20, choices=hello_choices, null=True)
    hi_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_hi = models.CharField(max_length=20, choices=hi_choices, null=True)
    lunch_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_lunch = models.CharField(max_length=20, choices=lunch_choices, null=True)
    nap_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_nap = models.CharField(max_length=20, choices=nap_choices, null=True)
    nightnight_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_nightnight = models.CharField(max_length=20, choices=nightnight_choices, null=True)
    no_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_no = models.CharField(max_length=20, choices=no_choices, null=True)
    pattycake_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_pattycake = models.CharField(max_length=20, choices=pattycake_choices, null=True)
    peekaboo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_peekaboo = models.CharField(max_length=20, choices=peekaboo_choices, null=True)
    please_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_please = models.CharField(max_length=20, choices=please_choices, null=True)
    shh_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_shh = models.CharField(max_length=20, choices=shh_choices, null=True)
    thank_you_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_thank_you = models.CharField(max_length=20, choices=thank_you_choices, null=True)
    wait_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_wait = models.CharField(max_length=20, choices=wait_choices, null=True)
    wanna_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_wanna = models.CharField(max_length=20, choices=wanna_choices, null=True)
    yes_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_yes = models.CharField(max_length=20, choices=yes_choices, null=True)
    bite_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_bite = models.CharField(max_length=20, choices=bite_choices, null=True)
    blow_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_blow = models.CharField(max_length=20, choices=blow_choices, null=True)
    break_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_break = models.CharField(max_length=20, choices=break_choices, null=True)
    bring_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_bring = models.CharField(max_length=20, choices=bring_choices, null=True)
    bump_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_bump = models.CharField(max_length=20, choices=bump_choices, null=True)
    clean_action_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_clean_action = models.CharField(max_length=20, choices=clean_action_choices, null=True)
    close_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_close = models.CharField(max_length=20, choices=close_choices, null=True)
    cry_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cry = models.CharField(max_length=20, choices=cry_choices, null=True)
    dance_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_dance = models.CharField(max_length=20, choices=dance_choices, null=True)
    draw_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_draw = models.CharField(max_length=20, choices=draw_choices, null=True)
    drink_action_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_drink_action = models.CharField(max_length=20, choices=drink_action_choices, null=True)
    drive_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_drive = models.CharField(max_length=20, choices=drive_choices, null=True)
    eat_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_eat = models.CharField(max_length=20, choices=eat_choices, null=True)
    fall_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_fall = models.CharField(max_length=20, choices=fall_choices, null=True)
    feed_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_feed = models.CharField(max_length=20, choices=feed_choices, null=True)
    finish_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_finish = models.CharField(max_length=20, choices=finish_choices, null=True)
    get_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_get = models.CharField(max_length=20, choices=get_choices, null=True)
    give_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_give = models.CharField(max_length=20, choices=give_choices, null=True)
    go_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_go = models.CharField(max_length=20, choices=go_choices, null=True)
    help_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_help = models.CharField(max_length=20, choices=help_choices, null=True)
    hit_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_hit = models.CharField(max_length=20, choices=hit_choices, null=True)
    hug_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_hug = models.CharField(max_length=20, choices=hug_choices, null=True)
    hurry_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_hurry = models.CharField(max_length=20, choices=hurry_choices, null=True)
    jump_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_jump = models.CharField(max_length=20, choices=jump_choices, null=True)
    kick_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_kick = models.CharField(max_length=20, choices=kick_choices, null=True)
    kiss_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_kiss = models.CharField(max_length=20, choices=kiss_choices, null=True)
    look_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_look = models.CharField(max_length=20, choices=look_choices, null=True)
    love_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_love = models.CharField(max_length=20, choices=love_choices, null=True)
    open_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_open = models.CharField(max_length=20, choices=open_choices, null=True)
    play_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_play = models.CharField(max_length=20, choices=play_choices, null=True)
    pull_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_pull = models.CharField(max_length=20, choices=pull_choices, null=True)
    push_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_push = models.CharField(max_length=20, choices=push_choices, null=True)
    put_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_put = models.CharField(max_length=20, choices=put_choices, null=True)
    read_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_read = models.CharField(max_length=20, choices=read_choices, null=True)
    ride_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_ride = models.CharField(max_length=20, choices=ride_choices, null=True)
    run_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_run = models.CharField(max_length=20, choices=run_choices, null=True)
    say_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_say = models.CharField(max_length=20, choices=say_choices, null=True)
    see_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_see = models.CharField(max_length=20, choices=see_choices, null=True)
    show_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_show = models.CharField(max_length=20, choices=show_choices, null=True)
    sing_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_sing = models.CharField(max_length=20, choices=sing_choices, null=True)
    sleep_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_sleep = models.CharField(max_length=20, choices=sleep_choices, null=True)
    smile_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_smile = models.CharField(max_length=20, choices=smile_choices, null=True)
    splash_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_splash = models.CharField(max_length=20, choices=splash_choices, null=True)
    stop_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_stop = models.CharField(max_length=20, choices=stop_choices, null=True)
    swim_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_swim = models.CharField(max_length=20, choices=swim_choices, null=True)
    swing_action_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_swing_action = models.CharField(max_length=20, choices=swing_action_choices, null=True)
    take_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_take = models.CharField(max_length=20, choices=take_choices, null=True)
    throw_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_throw = models.CharField(max_length=20, choices=throw_choices, null=True)
    tickle_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_tickle = models.CharField(max_length=20, choices=tickle_choices, null=True)
    touch_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_touch = models.CharField(max_length=20, choices=touch_choices, null=True)
    watch_action_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_watch_action = models.CharField(max_length=20, choices=watch_action_choices, null=True)
    walk_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_walk = models.CharField(max_length=20, choices=walk_choices, null=True)
    wash_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_wash = models.CharField(max_length=20, choices=wash_choices, null=True)
    wipe_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_wipe = models.CharField(max_length=20, choices=wipe_choices, null=True)
    write_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_write = models.CharField(max_length=20, choices=write_choices, null=True)
    day_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_day = models.CharField(max_length=20, choices=day_choices, null=True)
    later_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_later = models.CharField(max_length=20, choices=later_choices, null=True)
    morning_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_morning = models.CharField(max_length=20, choices=morning_choices, null=True)
    night_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_night = models.CharField(max_length=20, choices=night_choices, null=True)
    now_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_now = models.CharField(max_length=20, choices=now_choices, null=True)
    today_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_today = models.CharField(max_length=20, choices=today_choices, null=True)
    tomorrow_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_tomorrow = models.CharField(max_length=20, choices=tomorrow_choices, null=True)
    tonight_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_tonight = models.CharField(max_length=20, choices=tonight_choices, null=True)
    allgone_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_allgone = models.CharField(max_length=20, choices=allgone_choices, null=True)
    asleep_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_asleep = models.CharField(max_length=20, choices=asleep_choices, null=True)
    bad_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_bad = models.CharField(max_length=20, choices=bad_choices, null=True)
    big_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_big = models.CharField(max_length=20, choices=big_choices, null=True)
    blue_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_blue = models.CharField(max_length=20, choices=blue_choices, null=True)
    broken_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_broken = models.CharField(max_length=20, choices=broken_choices, null=True)
    careful_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_careful = models.CharField(max_length=20, choices=careful_choices, null=True)
    clean_description_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_clean_description = models.CharField(max_length=20, choices=clean_description_choices, null=True)
    cold_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cold = models.CharField(max_length=20, choices=cold_choices, null=True)
    cute_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cute = models.CharField(max_length=20, choices=cute_choices, null=True)
    dark_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_dark = models.CharField(max_length=20, choices=dark_choices, null=True)
    dirty_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_dirty = models.CharField(max_length=20, choices=dirty_choices, null=True)
    dry_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_dry = models.CharField(max_length=20, choices=dry_choices, null=True)
    empty_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_empty = models.CharField(max_length=20, choices=empty_choices, null=True)
    fast_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_fast = models.CharField(max_length=20, choices=fast_choices, null=True)
    fine_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_fine = models.CharField(max_length=20, choices=fine_choices, null=True)
    gentle_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_gentle = models.CharField(max_length=20, choices=gentle_choices, null=True)
    good_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_good = models.CharField(max_length=20, choices=good_choices, null=True)
    happy_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_happy = models.CharField(max_length=20, choices=happy_choices, null=True)
    hard_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_hard = models.CharField(max_length=20, choices=hard_choices, null=True)
    hot_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_hot = models.CharField(max_length=20, choices=hot_choices, null=True)
    hungry_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_hungry = models.CharField(max_length=20, choices=hungry_choices, null=True)
    hurt_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_hurt = models.CharField(max_length=20, choices=hurt_choices, null=True)
    little_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_little = models.CharField(max_length=20, choices=little_choices, null=True)
    naughty_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_naughty = models.CharField(max_length=20, choices=naughty_choices, null=True)
    nice_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_nice = models.CharField(max_length=20, choices=nice_choices, null=True)
    old_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_old = models.CharField(max_length=20, choices=old_choices, null=True)
    pretty_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_pretty = models.CharField(max_length=20, choices=pretty_choices, null=True)
    red_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_red = models.CharField(max_length=20, choices=red_choices, null=True)
    scared_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_scared = models.CharField(max_length=20, choices=scared_choices, null=True)
    sick_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_sick = models.CharField(max_length=20, choices=sick_choices, null=True)
    sleepy_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_sleepy = models.CharField(max_length=20, choices=sleepy_choices, null=True)
    soft_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_soft = models.CharField(max_length=20, choices=soft_choices, null=True)
    thirsty_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_thirsty = models.CharField(max_length=20, choices=thirsty_choices, null=True)
    tired_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_tired = models.CharField(max_length=20, choices=tired_choices, null=True)
    wet_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_wet = models.CharField(max_length=20, choices=wet_choices, null=True)
    yucky_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_yucky = models.CharField(max_length=20, choices=yucky_choices, null=True)
    his_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_his = models.CharField(max_length=20, choices=his_choices, null=True)
    her_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_her = models.CharField(max_length=20, choices=her_choices, null=True)
    i_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_i = models.CharField(max_length=20, choices=i_choices, null=True)
    it_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_it = models.CharField(max_length=20, choices=it_choices, null=True)
    me_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_me = models.CharField(max_length=20, choices=me_choices, null=True)
    mine_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_mine = models.CharField(max_length=20, choices=mine_choices, null=True)
    my_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_my = models.CharField(max_length=20, choices=my_choices, null=True)
    that_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_that = models.CharField(max_length=20, choices=that_choices, null=True)
    this_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_this = models.CharField(max_length=20, choices=this_choices, null=True)
    you_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_you = models.CharField(max_length=20, choices=you_choices, null=True)
    your_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_your = models.CharField(max_length=20, choices=your_choices, null=True)
    how_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_how = models.CharField(max_length=20, choices=how_choices, null=True)
    what_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_what = models.CharField(max_length=20, choices=what_choices, null=True)
    when_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_when = models.CharField(max_length=20, choices=when_choices, null=True)
    where_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_where = models.CharField(max_length=20, choices=where_choices, null=True)
    who_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_who = models.CharField(max_length=20, choices=who_choices, null=True)
    why_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_why = models.CharField(max_length=20, choices=why_choices, null=True)
    away_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_away = models.CharField(max_length=20, choices=away_choices, null=True)
    back_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_back = models.CharField(max_length=20, choices=back_choices, null=True)
    down_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_down = models.CharField(max_length=20, choices=down_choices, null=True)
    in_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_in = models.CharField(max_length=20, choices=in_choices, null=True)
    inside_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_inside = models.CharField(max_length=20, choices=inside_choices, null=True)
    off_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_off = models.CharField(max_length=20, choices=off_choices, null=True)
    on_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_on = models.CharField(max_length=20, choices=on_choices, null=True)
    out_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_out = models.CharField(max_length=20, choices=out_choices, null=True)
    there_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_there = models.CharField(max_length=20, choices=there_choices, null=True)
    under_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_under = models.CharField(max_length=20, choices=under_choices, null=True)
    up_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_up = models.CharField(max_length=20, choices=up_choices, null=True)
    all_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_all = models.CharField(max_length=20, choices=all_choices, null=True)
    another_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_another = models.CharField(max_length=20, choices=another_choices, null=True)
    more_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_more = models.CharField(max_length=20, choices=more_choices, null=True)
    none_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_none = models.CharField(max_length=20, choices=none_choices, null=True)
    not_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_not = models.CharField(max_length=20, choices=not_choices, null=True)
    other_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_other = models.CharField(max_length=20, choices=other_choices, null=True)
    same_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_same = models.CharField(max_length=20, choices=same_choices, null=True)
    some_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_some = models.CharField(max_length=20, choices=some_choices, null=True)
    armshow_choices = [(u'not yet', u'not yet'), (u'sometimes', u'sometimes'), (u'often', u'often')]
    item_armshow = models.CharField(max_length=20, choices=armshow_choices, null=True)
    reachout_choices = [(u'not yet', u'not yet'), (u'sometimes', u'sometimes'), (u'often', u'often')]
    item_reachout = models.CharField(max_length=20, choices=reachout_choices, null=True)
    points_choices = [(u'not yet', u'not yet'), (u'sometimes', u'sometimes'), (u'often', u'often')]
    item_points = models.CharField(max_length=20, choices=points_choices, null=True)
    waves_choices = [(u'not yet', u'not yet'), (u'sometimes', u'sometimes'), (u'often', u'often')]
    item_waves = models.CharField(max_length=20, choices=waves_choices, null=True)
    pickup_choices = [(u'not yet', u'not yet'), (u'sometimes', u'sometimes'), (u'often', u'often')]
    item_pickup = models.CharField(max_length=20, choices=pickup_choices, null=True)
    shakhead_choices = [(u'not yet', u'not yet'), (u'sometimes', u'sometimes'), (u'often', u'often')]
    item_shakhead = models.CharField(max_length=20, choices=shakhead_choices, null=True)
    nodhead_choices = [(u'not yet', u'not yet'), (u'sometimes', u'sometimes'), (u'often', u'often')]
    item_nodhead = models.CharField(max_length=20, choices=nodhead_choices, null=True)
    showhush_choices = [(u'not yet', u'not yet'), (u'sometimes', u'sometimes'), (u'often', u'often')]
    item_showhush = models.CharField(max_length=20, choices=showhush_choices, null=True)
    request_choices = [(u'not yet', u'not yet'), (u'sometimes', u'sometimes'), (u'often', u'often')]
    item_request = models.CharField(max_length=20, choices=request_choices, null=True)
    blowkiss_choices = [(u'not yet', u'not yet'), (u'sometimes', u'sometimes'), (u'often', u'often')]
    item_blowkiss = models.CharField(max_length=20, choices=blowkiss_choices, null=True)
    smacklip_choices = [(u'not yet', u'not yet'), (u'sometimes', u'sometimes'), (u'often', u'often')]
    item_smacklip = models.CharField(max_length=20, choices=smacklip_choices, null=True)
    shrugs_choices = [(u'not yet', u'not yet'), (u'sometimes', u'sometimes'), (u'often', u'often')]
    item_shrugs = models.CharField(max_length=20, choices=shrugs_choices, null=True)
    playpeek_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_playpeek = models.CharField(max_length=20, choices=playpeek_choices, null=True)
    patycak2_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_patycak2 = models.CharField(max_length=20, choices=patycak2_choices, null=True)
    sobig_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_sobig = models.CharField(max_length=20, choices=sobig_choices, null=True)
    chase_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_chase = models.CharField(max_length=20, choices=chase_choices, null=True)
    dosing_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_dosing = models.CharField(max_length=20, choices=dosing_choices, null=True)
    dodance_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_dodance = models.CharField(max_length=20, choices=dodance_choices, null=True)
    eatspoon_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_eatspoon = models.CharField(max_length=20, choices=eatspoon_choices, null=True)
    drinkcup_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_drinkcup = models.CharField(max_length=20, choices=drinkcup_choices, null=True)
    combhair_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_combhair = models.CharField(max_length=20, choices=combhair_choices, null=True)
    bshteeth_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_bshteeth = models.CharField(max_length=20, choices=bshteeth_choices, null=True)
    wipeface_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_wipeface = models.CharField(max_length=20, choices=wipeface_choices, null=True)
    puthat_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_puthat = models.CharField(max_length=20, choices=puthat_choices, null=True)
    putshoe_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_putshoe = models.CharField(max_length=20, choices=putshoe_choices, null=True)
    putwatch_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_putwatch = models.CharField(max_length=20, choices=putwatch_choices, null=True)
    ptdsleep_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_ptdsleep = models.CharField(max_length=20, choices=ptdsleep_choices, null=True)
    blowhot_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_blowhot = models.CharField(max_length=20, choices=blowhot_choices, null=True)
    flyplane_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_flyplane = models.CharField(max_length=20, choices=flyplane_choices, null=True)
    ptndtele_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_ptndtele = models.CharField(max_length=20, choices=ptndtele_choices, null=True)
    snifflow_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_snifflow = models.CharField(max_length=20, choices=snifflow_choices, null=True)
    pushcar_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_pushcar = models.CharField(max_length=20, choices=pushcar_choices, null=True)
    throwges_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_throwges = models.CharField(max_length=20, choices=throwges_choices, null=True)
    ptndpour_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_ptndpour = models.CharField(max_length=20, choices=ptndpour_choices, null=True)
    ptndstir_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_ptndstir = models.CharField(max_length=20, choices=ptndstir_choices, null=True)
    putobed_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_putobed = models.CharField(max_length=20, choices=putobed_choices, null=True)
    cover_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_cover = models.CharField(max_length=20, choices=cover_choices, null=True)
    feedbotl_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_feedbotl = models.CharField(max_length=20, choices=feedbotl_choices, null=True)
    feedspon_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_feedspon = models.CharField(max_length=20, choices=feedspon_choices, null=True)
    brushit_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_brushit = models.CharField(max_length=20, choices=brushit_choices, null=True)
    burbit_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_burbit = models.CharField(max_length=20, choices=burbit_choices, null=True)
    pushit_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_pushit = models.CharField(max_length=20, choices=pushit_choices, null=True)
    rockit_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_rockit = models.CharField(max_length=20, choices=rockit_choices, null=True)
    kissit_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_kissit = models.CharField(max_length=20, choices=kissit_choices, null=True)
    dressit_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_dressit = models.CharField(max_length=20, choices=dressit_choices, null=True)
    wipeit_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_wipeit = models.CharField(max_length=20, choices=wipeit_choices, null=True)
    talkit_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_talkit = models.CharField(max_length=20, choices=talkit_choices, null=True)
    diaperit_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_diaperit = models.CharField(max_length=20, choices=diaperit_choices, null=True)
    sweep_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_sweep = models.CharField(max_length=20, choices=sweep_choices, null=True)
    putkey_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_putkey = models.CharField(max_length=20, choices=putkey_choices, null=True)
    pound_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_pound = models.CharField(max_length=20, choices=pound_choices, null=True)
    usesaw_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_usesaw = models.CharField(max_length=20, choices=usesaw_choices, null=True)
    type_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_type = models.CharField(max_length=20, choices=type_choices, null=True)
    ptndread_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_ptndread = models.CharField(max_length=20, choices=ptndread_choices, null=True)
    dovacuum_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_dovacuum = models.CharField(max_length=20, choices=dovacuum_choices, null=True)
    waterplt_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_waterplt = models.CharField(max_length=20, choices=waterplt_choices, null=True)
    playmus_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_playmus = models.CharField(max_length=20, choices=playmus_choices, null=True)
    ptnddriv_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_ptnddriv = models.CharField(max_length=20, choices=ptnddriv_choices, null=True)
    washdish_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_washdish = models.CharField(max_length=20, choices=washdish_choices, null=True)
    usecloth_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_usecloth = models.CharField(max_length=20, choices=usecloth_choices, null=True)
    usepen_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_usepen = models.CharField(max_length=20, choices=usepen_choices, null=True)
    dig_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_dig = models.CharField(max_length=20, choices=dig_choices, null=True)
    wearglas_choices = [(u'yes', u'yes'), (u'no', u'no')]
    item_wearglas = models.CharField(max_length=20, choices=wearglas_choices, null=True)


class Spanish_WS(BaseTable):
    tutu_choices = [(u'produces', u'produces')]
    item_tutu = models.CharField(max_length=20, choices=tutu_choices, null=True)
    qiqiriqi_choices = [(u'produces', u'produces')]
    item_qiqiriqi = models.CharField(max_length=20, choices=qiqiriqi_choices, null=True)
    pum_choices = [(u'produces', u'produces')]
    item_pum = models.CharField(max_length=20, choices=pum_choices, null=True)
    pipi_choices = [(u'produces', u'produces')]
    item_pipi = models.CharField(max_length=20, choices=pipi_choices, null=True)
    piopio_choices = [(u'produces', u'produces')]
    item_piopio = models.CharField(max_length=20, choices=piopio_choices, null=True)
    muu_choices = [(u'produces', u'produces')]
    item_muu = models.CharField(max_length=20, choices=muu_choices, null=True)
    miau_choices = [(u'produces', u'produces')]
    item_miau = models.CharField(max_length=20, choices=miau_choices, null=True)
    guagua_choices = [(u'produces', u'produces')]
    item_guagua = models.CharField(max_length=20, choices=guagua_choices, null=True)
    cuacua_choices = [(u'produces', u'produces')]
    item_cuacua = models.CharField(max_length=20, choices=cuacua_choices, null=True)
    beemee_choices = [(u'produces', u'produces')]
    item_beemee = models.CharField(max_length=20, choices=beemee_choices, null=True)
    am_choices = [(u'produces', u'produces')]
    item_am = models.CharField(max_length=20, choices=am_choices, null=True)
    ay_choices = [(u'produces', u'produces')]
    item_ay = models.CharField(max_length=20, choices=ay_choices, null=True)
    vibora_choices = [(u'produces', u'produces')]
    item_vibora = models.CharField(max_length=20, choices=vibora_choices, null=True)
    venado_choices = [(u'produces', u'produces')]
    item_venado = models.CharField(max_length=20, choices=venado_choices, null=True)
    vaca_choices = [(u'produces', u'produces')]
    item_vaca = models.CharField(max_length=20, choices=vaca_choices, null=True)
    tortuga_choices = [(u'produces', u'produces')]
    item_tortuga = models.CharField(max_length=20, choices=tortuga_choices, null=True)
    tigre_choices = [(u'produces', u'produces')]
    item_tigre = models.CharField(max_length=20, choices=tigre_choices, null=True)
    raton_choices = [(u'produces', u'produces')]
    item_raton = models.CharField(max_length=20, choices=raton_choices, null=True)
    rano_choices = [(u'produces', u'produces')]
    item_rano = models.CharField(max_length=20, choices=rano_choices, null=True)
    puerco_choices = [(u'produces', u'produces')]
    item_puerco = models.CharField(max_length=20, choices=puerco_choices, null=True)
    pollito_choices = [(u'produces', u'produces')]
    item_pollito = models.CharField(max_length=20, choices=pollito_choices, null=True)
    pinguino_choices = [(u'produces', u'produces')]
    item_pinguino = models.CharField(max_length=20, choices=pinguino_choices, null=True)
    pescado1_choices = [(u'produces', u'produces')]
    item_pescado1 = models.CharField(max_length=20, choices=pescado1_choices, null=True)
    perro_choices = [(u'produces', u'produces')]
    item_perro = models.CharField(max_length=20, choices=perro_choices, null=True)
    pato_choices = [(u'produces', u'produces')]
    item_pato = models.CharField(max_length=20, choices=pato_choices, null=True)
    pajaro_choices = [(u'produces', u'produces')]
    item_pajaro = models.CharField(max_length=20, choices=pajaro_choices, null=True)
    oso_choices = [(u'produces', u'produces')]
    item_oso = models.CharField(max_length=20, choices=oso_choices, null=True)
    mosco_choices = [(u'produces', u'produces')]
    item_mosco = models.CharField(max_length=20, choices=mosco_choices, null=True)
    mosca_choices = [(u'produces', u'produces')]
    item_mosca = models.CharField(max_length=20, choices=mosca_choices, null=True)
    mono_choices = [(u'produces', u'produces')]
    item_mono = models.CharField(max_length=20, choices=mono_choices, null=True)
    mariposa_choices = [(u'produces', u'produces')]
    item_mariposa = models.CharField(max_length=20, choices=mariposa_choices, null=True)
    lobo_choices = [(u'produces', u'produces')]
    item_lobo = models.CharField(max_length=20, choices=lobo_choices, null=True)
    leon_choices = [(u'produces', u'produces')]
    item_leon = models.CharField(max_length=20, choices=leon_choices, null=True)
    jirafa_choices = [(u'produces', u'produces')]
    item_jirafa = models.CharField(max_length=20, choices=jirafa_choices, null=True)
    hormiga_choices = [(u'produces', u'produces')]
    item_hormiga = models.CharField(max_length=20, choices=hormiga_choices, null=True)
    hippotmo_choices = [(u'produces', u'produces')]
    item_hippotmo = models.CharField(max_length=20, choices=hippotmo_choices, null=True)
    guajolot_choices = [(u'produces', u'produces')]
    item_guajolot = models.CharField(max_length=20, choices=guajolot_choices, null=True)
    gato_choices = [(u'produces', u'produces')]
    item_gato = models.CharField(max_length=20, choices=gato_choices, null=True)
    ganso_choices = [(u'produces', u'produces')]
    item_ganso = models.CharField(max_length=20, choices=ganso_choices, null=True)
    gallina_choices = [(u'produces', u'produces')]
    item_gallina = models.CharField(max_length=20, choices=gallina_choices, null=True)
    foca_choices = [(u'produces', u'produces')]
    item_foca = models.CharField(max_length=20, choices=foca_choices, null=True)
    elefante_choices = [(u'produces', u'produces')]
    item_elefante = models.CharField(max_length=20, choices=elefante_choices, null=True)
    conejo_choices = [(u'produces', u'produces')]
    item_conejo = models.CharField(max_length=20, choices=conejo_choices, null=True)
    cocdrilo_choices = [(u'produces', u'produces')]
    item_cocdrilo = models.CharField(max_length=20, choices=cocdrilo_choices, null=True)
    cebra_choices = [(u'produces', u'produces')]
    item_cebra = models.CharField(max_length=20, choices=cebra_choices, null=True)
    caballo_choices = [(u'produces', u'produces')]
    item_caballo = models.CharField(max_length=20, choices=caballo_choices, null=True)
    burro_choices = [(u'produces', u'produces')]
    item_burro = models.CharField(max_length=20, choices=burro_choices, null=True)
    buho_choices = [(u'produces', u'produces')]
    item_buho = models.CharField(max_length=20, choices=buho_choices, null=True)
    buey_choices = [(u'produces', u'produces')]
    item_buey = models.CharField(max_length=20, choices=buey_choices, null=True)
    borrego_choices = [(u'produces', u'produces')]
    item_borrego = models.CharField(max_length=20, choices=borrego_choices, null=True)
    bicho_choices = [(u'produces', u'produces')]
    item_bicho = models.CharField(max_length=20, choices=bicho_choices, null=True)
    ardilla_choices = [(u'produces', u'produces')]
    item_ardilla = models.CharField(max_length=20, choices=ardilla_choices, null=True)
    arana_choices = [(u'produces', u'produces')]
    item_arana = models.CharField(max_length=20, choices=arana_choices, null=True)
    animal_choices = [(u'produces', u'produces')]
    item_animal = models.CharField(max_length=20, choices=animal_choices, null=True)
    abeja_choices = [(u'produces', u'produces')]
    item_abeja = models.CharField(max_length=20, choices=abeja_choices, null=True)
    trineo_choices = [(u'produces', u'produces')]
    item_trineo = models.CharField(max_length=20, choices=trineo_choices, null=True)
    tricicl1_choices = [(u'produces', u'produces')]
    item_tricicl1 = models.CharField(max_length=20, choices=tricicl1_choices, null=True)
    tren_choices = [(u'produces', u'produces')]
    item_tren = models.CharField(max_length=20, choices=tren_choices, null=True)
    tractor_choices = [(u'produces', u'produces')]
    item_tractor = models.CharField(max_length=20, choices=tractor_choices, null=True)
    moto_choices = [(u'produces', u'produces')]
    item_moto = models.CharField(max_length=20, choices=moto_choices, null=True)
    helicptr_choices = [(u'produces', u'produces')]
    item_helicptr = models.CharField(max_length=20, choices=helicptr_choices, null=True)
    carro_choices = [(u'produces', u'produces')]
    item_carro = models.CharField(max_length=20, choices=carro_choices, null=True)
    carreola_choices = [(u'produces', u'produces')]
    item_carreola = models.CharField(max_length=20, choices=carreola_choices, null=True)
    camion_choices = [(u'produces', u'produces')]
    item_camion = models.CharField(max_length=20, choices=camion_choices, null=True)
    camibomb_choices = [(u'produces', u'produces')]
    item_camibomb = models.CharField(max_length=20, choices=camibomb_choices, null=True)
    biciclet_choices = [(u'produces', u'produces')]
    item_biciclet = models.CharField(max_length=20, choices=biciclet_choices, null=True)
    barco_choices = [(u'produces', u'produces')]
    item_barco = models.CharField(max_length=20, choices=barco_choices, null=True)
    avion_choices = [(u'produces', u'produces')]
    item_avion = models.CharField(max_length=20, choices=avion_choices, null=True)
    autobus_choices = [(u'produces', u'produces')]
    item_autobus = models.CharField(max_length=20, choices=autobus_choices, null=True)
    agua_choices = [(u'produces', u'produces')]
    item_agua = models.CharField(max_length=20, choices=agua_choices, null=True)
    arroz_choices = [(u'produces', u'produces')]
    item_arroz = models.CharField(max_length=20, choices=arroz_choices, null=True)
    atole_choices = [(u'produces', u'produces')]
    item_atole = models.CharField(max_length=20, choices=atole_choices, null=True)
    atun_choices = [(u'produces', u'produces')]
    item_atun = models.CharField(max_length=20, choices=atun_choices, null=True)
    azucar_choices = [(u'produces', u'produces')]
    item_azucar = models.CharField(max_length=20, choices=azucar_choices, null=True)
    cafe_choices = [(u'produces', u'produces')]
    item_cafe = models.CharField(max_length=20, choices=cafe_choices, null=True)
    calabaza_choices = [(u'produces', u'produces')]
    item_calabaza = models.CharField(max_length=20, choices=calabaza_choices, null=True)
    carne_choices = [(u'produces', u'produces')]
    item_carne = models.CharField(max_length=20, choices=carne_choices, null=True)
    cereal_choices = [(u'produces', u'produces')]
    item_cereal = models.CharField(max_length=20, choices=cereal_choices, null=True)
    chicharo_choices = [(u'produces', u'produces')]
    item_chicharo = models.CharField(max_length=20, choices=chicharo_choices, null=True)
    chicle_choices = [(u'produces', u'produces')]
    item_chicle = models.CharField(max_length=20, choices=chicle_choices, null=True)
    chile_choices = [(u'produces', u'produces')]
    item_chile = models.CharField(max_length=20, choices=chile_choices, null=True)
    chocolat_choices = [(u'produces', u'produces')]
    item_chocolat = models.CharField(max_length=20, choices=chocolat_choices, null=True)
    comida_choices = [(u'produces', u'produces')]
    item_comida = models.CharField(max_length=20, choices=comida_choices, null=True)
    dulce_choices = [(u'produces', u'produces')]
    item_dulce = models.CharField(max_length=20, choices=dulce_choices, null=True)
    durazno_choices = [(u'produces', u'produces')]
    item_durazno = models.CharField(max_length=20, choices=durazno_choices, null=True)
    ejotes_choices = [(u'produces', u'produces')]
    item_ejotes = models.CharField(max_length=20, choices=ejotes_choices, null=True)
    elote_choices = [(u'produces', u'produces')]
    item_elote = models.CharField(max_length=20, choices=elote_choices, null=True)
    espgueti_choices = [(u'produces', u'produces')]
    item_espgueti = models.CharField(max_length=20, choices=espgueti_choices, null=True)
    fresa_choices = [(u'produces', u'produces')]
    item_fresa = models.CharField(max_length=20, choices=fresa_choices, null=True)
    frijoles_choices = [(u'produces', u'produces')]
    item_frijoles = models.CharField(max_length=20, choices=frijoles_choices, null=True)
    galleta_choices = [(u'produces', u'produces')]
    item_galleta = models.CharField(max_length=20, choices=galleta_choices, null=True)
    gellatin_choices = [(u'produces', u'produces')]
    item_gellatin = models.CharField(max_length=20, choices=gellatin_choices, null=True)
    hamburgs_choices = [(u'produces', u'produces')]
    item_hamburgs = models.CharField(max_length=20, choices=hamburgs_choices, null=True)
    helado_choices = [(u'produces', u'produces')]
    item_helado = models.CharField(max_length=20, choices=helado_choices, null=True)
    hielo_choices = [(u'produces', u'produces')]
    item_hielo = models.CharField(max_length=20, choices=hielo_choices, null=True)
    hotcakes_choices = [(u'produces', u'produces')]
    item_hotcakes = models.CharField(max_length=20, choices=hotcakes_choices, null=True)
    huevo_choices = [(u'produces', u'produces')]
    item_huevo = models.CharField(max_length=20, choices=huevo_choices, null=True)
    jamon_choices = [(u'produces', u'produces')]
    item_jamon = models.CharField(max_length=20, choices=jamon_choices, null=True)
    jugo_choices = [(u'produces', u'produces')]
    item_jugo = models.CharField(max_length=20, choices=jugo_choices, null=True)
    leche_choices = [(u'produces', u'produces')]
    item_leche = models.CharField(max_length=20, choices=leche_choices, null=True)
    licuado_choices = [(u'produces', u'produces')]
    item_licuado = models.CharField(max_length=20, choices=licuado_choices, null=True)
    limonad_choices = [(u'produces', u'produces')]
    item_limonad = models.CharField(max_length=20, choices=limonad_choices, null=True)
    mani_choices = [(u'produces', u'produces')]
    item_mani = models.CharField(max_length=20, choices=mani_choices, null=True)
    mantqila_choices = [(u'produces', u'produces')]
    item_mantqila = models.CharField(max_length=20, choices=mantqila_choices, null=True)
    manzana_choices = [(u'produces', u'produces')]
    item_manzana = models.CharField(max_length=20, choices=manzana_choices, null=True)
    melon_choices = [(u'produces', u'produces')]
    item_melon = models.CharField(max_length=20, choices=melon_choices, null=True)
    mermelad_choices = [(u'produces', u'produces')]
    item_mermelad = models.CharField(max_length=20, choices=mermelad_choices, null=True)
    naranja_choices = [(u'produces', u'produces')]
    item_naranja = models.CharField(max_length=20, choices=naranja_choices, null=True)
    paleta_choices = [(u'produces', u'produces')]
    item_paleta = models.CharField(max_length=20, choices=paleta_choices, null=True)
    palomtas_choices = [(u'produces', u'produces')]
    item_palomtas = models.CharField(max_length=20, choices=palomtas_choices, null=True)
    pan_choices = [(u'produces', u'produces')]
    item_pan = models.CharField(max_length=20, choices=pan_choices, null=True)
    pandulc_choices = [(u'produces', u'produces')]
    item_pandulc = models.CharField(max_length=20, choices=pandulc_choices, null=True)
    papas_choices = [(u'produces', u'produces')]
    item_papas = models.CharField(max_length=20, choices=papas_choices, null=True)
    papitas_choices = [(u'produces', u'produces')]
    item_papitas = models.CharField(max_length=20, choices=papitas_choices, null=True)
    pasas_choices = [(u'produces', u'produces')]
    item_pasas = models.CharField(max_length=20, choices=pasas_choices, null=True)
    pastel_choices = [(u'produces', u'produces')]
    item_pastel = models.CharField(max_length=20, choices=pastel_choices, null=True)
    pentbttr_choices = [(u'produces', u'produces')]
    item_pentbttr = models.CharField(max_length=20, choices=pentbttr_choices, null=True)
    pescado2_choices = [(u'produces', u'produces')]
    item_pescado2 = models.CharField(max_length=20, choices=pescado2_choices, null=True)
    platano_choices = [(u'produces', u'produces')]
    item_platano = models.CharField(max_length=20, choices=platano_choices, null=True)
    pollo_choices = [(u'produces', u'produces')]
    item_pollo = models.CharField(max_length=20, choices=pollo_choices, null=True)
    quesdila_choices = [(u'produces', u'produces')]
    item_quesdila = models.CharField(max_length=20, choices=quesdila_choices, null=True)
    queso_choices = [(u'produces', u'produces')]
    item_queso = models.CharField(max_length=20, choices=queso_choices, null=True)
    sal_choices = [(u'produces', u'produces')]
    item_sal = models.CharField(max_length=20, choices=sal_choices, null=True)
    salchch_choices = [(u'produces', u'produces')]
    item_salchch = models.CharField(max_length=20, choices=salchch_choices, null=True)
    salsa_choices = [(u'produces', u'produces')]
    item_salsa = models.CharField(max_length=20, choices=salsa_choices, null=True)
    sandia_choices = [(u'produces', u'produces')]
    item_sandia = models.CharField(max_length=20, choices=sandia_choices, null=True)
    soda_choices = [(u'produces', u'produces')]
    item_soda = models.CharField(max_length=20, choices=soda_choices, null=True)
    sopa_choices = [(u'produces', u'produces')]
    item_sopa = models.CharField(max_length=20, choices=sopa_choices, null=True)
    taco_choices = [(u'produces', u'produces')]
    item_taco = models.CharField(max_length=20, choices=taco_choices, null=True)
    te1_choices = [(u'produces', u'produces')]
    item_te1 = models.CharField(max_length=20, choices=te1_choices, null=True)
    torta_choices = [(u'produces', u'produces')]
    item_torta = models.CharField(max_length=20, choices=torta_choices, null=True)
    tortila_choices = [(u'produces', u'produces')]
    item_tortila = models.CharField(max_length=20, choices=tortila_choices, null=True)
    uvas_choices = [(u'produces', u'produces')]
    item_uvas = models.CharField(max_length=20, choices=uvas_choices, null=True)
    vainilla_choices = [(u'produces', u'produces')]
    item_vainilla = models.CharField(max_length=20, choices=vainilla_choices, null=True)
    vitamina_choices = [(u'produces', u'produces')]
    item_vitamina = models.CharField(max_length=20, choices=vitamina_choices, null=True)
    yoghurt_choices = [(u'produces', u'produces')]
    item_yoghurt = models.CharField(max_length=20, choices=yoghurt_choices, null=True)
    zanahori_choices = [(u'produces', u'produces')]
    item_zanahori = models.CharField(max_length=20, choices=zanahori_choices, null=True)
    boton_choices = [(u'produces', u'produces')]
    item_boton = models.CharField(max_length=20, choices=boton_choices, null=True)
    bufanda_choices = [(u'produces', u'produces')]
    item_bufanda = models.CharField(max_length=20, choices=bufanda_choices, null=True)
    calcetin_choices = [(u'produces', u'produces')]
    item_calcetin = models.CharField(max_length=20, choices=calcetin_choices, null=True)
    calzon_choices = [(u'produces', u'produces')]
    item_calzon = models.CharField(max_length=20, choices=calzon_choices, null=True)
    camisa_choices = [(u'produces', u'produces')]
    item_camisa = models.CharField(max_length=20, choices=camisa_choices, null=True)
    chancla_choices = [(u'produces', u'produces')]
    item_chancla = models.CharField(max_length=20, choices=chancla_choices, null=True)
    cierre_choices = [(u'produces', u'produces')]
    item_cierre = models.CharField(max_length=20, choices=cierre_choices, null=True)
    collar_choices = [(u'produces', u'produces')]
    item_collar = models.CharField(max_length=20, choices=collar_choices, null=True)
    falda_choices = [(u'produces', u'produces')]
    item_falda = models.CharField(max_length=20, choices=falda_choices, null=True)
    gorra_choices = [(u'produces', u'produces')]
    item_gorra = models.CharField(max_length=20, choices=gorra_choices, null=True)
    guantes_choices = [(u'produces', u'produces')]
    item_guantes = models.CharField(max_length=20, choices=guantes_choices, null=True)
    lentes_choices = [(u'produces', u'produces')]
    item_lentes = models.CharField(max_length=20, choices=lentes_choices, null=True)
    medias_choices = [(u'produces', u'produces')]
    item_medias = models.CharField(max_length=20, choices=medias_choices, null=True)
    panal_choices = [(u'produces', u'produces')]
    item_panal = models.CharField(max_length=20, choices=panal_choices, null=True)
    pantalon_choices = [(u'produces', u'produces')]
    item_pantalon = models.CharField(max_length=20, choices=pantalon_choices, null=True)
    pijama_choices = [(u'produces', u'produces')]
    item_pijama = models.CharField(max_length=20, choices=pijama_choices, null=True)
    playera_choices = [(u'produces', u'produces')]
    item_playera = models.CharField(max_length=20, choices=playera_choices, null=True)
    ropas_choices = [(u'produces', u'produces')]
    item_ropas = models.CharField(max_length=20, choices=ropas_choices, null=True)
    shorts_choices = [(u'produces', u'produces')]
    item_shorts = models.CharField(max_length=20, choices=shorts_choices, null=True)
    sombrero_choices = [(u'produces', u'produces')]
    item_sombrero = models.CharField(max_length=20, choices=sombrero_choices, null=True)
    sueter_choices = [(u'produces', u'produces')]
    item_sueter = models.CharField(max_length=20, choices=sueter_choices, null=True)
    vestido_choices = [(u'produces', u'produces')]
    item_vestido = models.CharField(max_length=20, choices=vestido_choices, null=True)
    zapato_choices = [(u'produces', u'produces')]
    item_zapato = models.CharField(max_length=20, choices=zapato_choices, null=True)
    barba_choices = [(u'produces', u'produces')]
    item_barba = models.CharField(max_length=20, choices=barba_choices, null=True)
    bigote_choices = [(u'produces', u'produces')]
    item_bigote = models.CharField(max_length=20, choices=bigote_choices, null=True)
    boca_choices = [(u'produces', u'produces')]
    item_boca = models.CharField(max_length=20, choices=boca_choices, null=True)
    brazo_choices = [(u'produces', u'produces')]
    item_brazo = models.CharField(max_length=20, choices=brazo_choices, null=True)
    cabeza_choices = [(u'produces', u'produces')]
    item_cabeza = models.CharField(max_length=20, choices=cabeza_choices, null=True)
    cachete_choices = [(u'produces', u'produces')]
    item_cachete = models.CharField(max_length=20, choices=cachete_choices, null=True)
    cara_choices = [(u'produces', u'produces')]
    item_cara = models.CharField(max_length=20, choices=cara_choices, null=True)
    chichi_choices = [(u'produces', u'produces')]
    item_chichi = models.CharField(max_length=20, choices=chichi_choices, null=True)
    dedo_choices = [(u'produces', u'produces')]
    item_dedo = models.CharField(max_length=20, choices=dedo_choices, null=True)
    dientes_choices = [(u'produces', u'produces')]
    item_dientes = models.CharField(max_length=20, choices=dientes_choices, null=True)
    gargnta_choices = [(u'produces', u'produces')]
    item_gargnta = models.CharField(max_length=20, choices=gargnta_choices, null=True)
    hombro_choices = [(u'produces', u'produces')]
    item_hombro = models.CharField(max_length=20, choices=hombro_choices, null=True)
    labios_choices = [(u'produces', u'produces')]
    item_labios = models.CharField(max_length=20, choices=labios_choices, null=True)
    lengua_choices = [(u'produces', u'produces')]
    item_lengua = models.CharField(max_length=20, choices=lengua_choices, null=True)
    mano_choices = [(u'produces', u'produces')]
    item_mano = models.CharField(max_length=20, choices=mano_choices, null=True)
    nalgas_choices = [(u'produces', u'produces')]
    item_nalgas = models.CharField(max_length=20, choices=nalgas_choices, null=True)
    nariz_choices = [(u'produces', u'produces')]
    item_nariz = models.CharField(max_length=20, choices=nariz_choices, null=True)
    ojos_choices = [(u'produces', u'produces')]
    item_ojos = models.CharField(max_length=20, choices=ojos_choices, null=True)
    ombligo_choices = [(u'produces', u'produces')]
    item_ombligo = models.CharField(max_length=20, choices=ombligo_choices, null=True)
    oreja_choices = [(u'produces', u'produces')]
    item_oreja = models.CharField(max_length=20, choices=oreja_choices, null=True)
    panza_choices = [(u'produces', u'produces')]
    item_panza = models.CharField(max_length=20, choices=panza_choices, null=True)
    pelo_choices = [(u'produces', u'produces')]
    item_pelo = models.CharField(max_length=20, choices=pelo_choices, null=True)
    pene_choices = [(u'produces', u'produces')]
    item_pene = models.CharField(max_length=20, choices=pene_choices, null=True)
    piernas_choices = [(u'produces', u'produces')]
    item_piernas = models.CharField(max_length=20, choices=piernas_choices, null=True)
    pies_choices = [(u'produces', u'produces')]
    item_pies = models.CharField(max_length=20, choices=pies_choices, null=True)
    rodilla_choices = [(u'produces', u'produces')]
    item_rodilla = models.CharField(max_length=20, choices=rodilla_choices, null=True)
    vagina_choices = [(u'produces', u'produces')]
    item_vagina = models.CharField(max_length=20, choices=vagina_choices, null=True)
    bat_choices = [(u'produces', u'produces')]
    item_bat = models.CharField(max_length=20, choices=bat_choices, null=True)
    burbujas_choices = [(u'produces', u'produces')]
    item_burbujas = models.CharField(max_length=20, choices=burbujas_choices, null=True)
    colores_choices = [(u'produces', u'produces')]
    item_colores = models.CharField(max_length=20, choices=colores_choices, null=True)
    crayolas_choices = [(u'produces', u'produces')]
    item_crayolas = models.CharField(max_length=20, choices=crayolas_choices, null=True)
    globo_choices = [(u'produces', u'produces')]
    item_globo = models.CharField(max_length=20, choices=globo_choices, null=True)
    hoja_choices = [(u'produces', u'produces')]
    item_hoja = models.CharField(max_length=20, choices=hoja_choices, null=True)
    juguete_choices = [(u'produces', u'produces')]
    item_juguete = models.CharField(max_length=20, choices=juguete_choices, null=True)
    lapiz_choices = [(u'produces', u'produces')]
    item_lapiz = models.CharField(max_length=20, choices=lapiz_choices, null=True)
    libro_choices = [(u'produces', u'produces')]
    item_libro = models.CharField(max_length=20, choices=libro_choices, null=True)
    muneca_choices = [(u'produces', u'produces')]
    item_muneca = models.CharField(max_length=20, choices=muneca_choices, null=True)
    osito_choices = [(u'produces', u'produces')]
    item_osito = models.CharField(max_length=20, choices=osito_choices, null=True)
    patines_choices = [(u'produces', u'produces')]
    item_patines = models.CharField(max_length=20, choices=patines_choices, null=True)
    pelota_choices = [(u'produces', u'produces')]
    item_pelota = models.CharField(max_length=20, choices=pelota_choices, null=True)
    pintura_choices = [(u'produces', u'produces')]
    item_pintura = models.CharField(max_length=20, choices=pintura_choices, null=True)
    plastlin_choices = [(u'produces', u'produces')]
    item_plastlin = models.CharField(max_length=20, choices=plastlin_choices, null=True)
    pluma_choices = [(u'produces', u'produces')]
    item_pluma = models.CharField(max_length=20, choices=pluma_choices, null=True)
    tambor_choices = [(u'produces', u'produces')]
    item_tambor = models.CharField(max_length=20, choices=tambor_choices, null=True)
    tricicl2_choices = [(u'produces', u'produces')]
    item_tricicl2 = models.CharField(max_length=20, choices=tricicl2_choices, null=True)
    botas_choices = [(u'produces', u'produces')]
    item_botas = models.CharField(max_length=20, choices=botas_choices, null=True)
    bolsa1_choices = [(u'produces', u'produces')]
    item_bolsa1 = models.CharField(max_length=20, choices=bolsa1_choices, null=True)
    babera_choices = [(u'produces', u'produces')]
    item_babera = models.CharField(max_length=20, choices=babera_choices, null=True)
    aretes_choices = [(u'produces', u'produces')]
    item_aretes = models.CharField(max_length=20, choices=aretes_choices, null=True)
    abrigo_choices = [(u'produces', u'produces')]
    item_abrigo = models.CharField(max_length=20, choices=abrigo_choices, null=True)
    almohada_choices = [(u'produces', u'produces')]
    item_almohada = models.CharField(max_length=20, choices=almohada_choices, null=True)
    aspirdor_choices = [(u'produces', u'produces')]
    item_aspirdor = models.CharField(max_length=20, choices=aspirdor_choices, null=True)
    basura_choices = [(u'produces', u'produces')]
    item_basura = models.CharField(max_length=20, choices=basura_choices, null=True)
    bolsa2_choices = [(u'produces', u'produces')]
    item_bolsa2 = models.CharField(max_length=20, choices=bolsa2_choices, null=True)
    botlmaml_choices = [(u'produces', u'produces')]
    item_botlmaml = models.CharField(max_length=20, choices=botlmaml_choices, null=True)
    caja_choices = [(u'produces', u'produces')]
    item_caja = models.CharField(max_length=20, choices=caja_choices, null=True)
    camara_choices = [(u'produces', u'produces')]
    item_camara = models.CharField(max_length=20, choices=camara_choices, null=True)
    canasta_choices = [(u'produces', u'produces')]
    item_canasta = models.CharField(max_length=20, choices=canasta_choices, null=True)
    cassette_choices = [(u'produces', u'produces')]
    item_cassette = models.CharField(max_length=20, choices=cassette_choices, null=True)
    cepidnte_choices = [(u'produces', u'produces')]
    item_cepidnte = models.CharField(max_length=20, choices=cepidnte_choices, null=True)
    cepillo_choices = [(u'produces', u'produces')]
    item_cepillo = models.CharField(max_length=20, choices=cepillo_choices, null=True)
    cerills_choices = [(u'produces', u'produces')]
    item_cerills = models.CharField(max_length=20, choices=cerills_choices, null=True)
    chupete_choices = [(u'produces', u'produces')]
    item_chupete = models.CharField(max_length=20, choices=chupete_choices, null=True)
    cigarrs_choices = [(u'produces', u'produces')]
    item_cigarrs = models.CharField(max_length=20, choices=cigarrs_choices, null=True)
    clavo_choices = [(u'produces', u'produces')]
    item_clavo = models.CharField(max_length=20, choices=clavo_choices, null=True)
    cobija_choices = [(u'produces', u'produces')]
    item_cobija = models.CharField(max_length=20, choices=cobija_choices, null=True)
    cuadro_choices = [(u'produces', u'produces')]
    item_cuadro = models.CharField(max_length=20, choices=cuadro_choices, null=True)
    cubeta_choices = [(u'produces', u'produces')]
    item_cubeta = models.CharField(max_length=20, choices=cubeta_choices, null=True)
    cuchara_choices = [(u'produces', u'produces')]
    item_cuchara = models.CharField(max_length=20, choices=cuchara_choices, null=True)
    cuchillo_choices = [(u'produces', u'produces')]
    item_cuchillo = models.CharField(max_length=20, choices=cuchillo_choices, null=True)
    dinero_choices = [(u'produces', u'produces')]
    item_dinero = models.CharField(max_length=20, choices=dinero_choices, null=True)
    escoba_choices = [(u'produces', u'produces')]
    item_escoba = models.CharField(max_length=20, choices=escoba_choices, null=True)
    espejo_choices = [(u'produces', u'produces')]
    item_espejo = models.CharField(max_length=20, choices=espejo_choices, null=True)
    fotos_choices = [(u'produces', u'produces')]
    item_fotos = models.CharField(max_length=20, choices=fotos_choices, null=True)
    jabon_choices = [(u'produces', u'produces')]
    item_jabon = models.CharField(max_length=20, choices=jabon_choices, null=True)
    lampara_choices = [(u'produces', u'produces')]
    item_lampara = models.CharField(max_length=20, choices=lampara_choices, null=True)
    llave_choices = [(u'produces', u'produces')]
    item_llave = models.CharField(max_length=20, choices=llave_choices, null=True)
    luz_choices = [(u'produces', u'produces')]
    item_luz = models.CharField(max_length=20, choices=luz_choices, null=True)
    martillo_choices = [(u'produces', u'produces')]
    item_martillo = models.CharField(max_length=20, choices=martillo_choices, null=True)
    medicina_choices = [(u'produces', u'produces')]
    item_medicina = models.CharField(max_length=20, choices=medicina_choices, null=True)
    olla_choices = [(u'produces', u'produces')]
    item_olla = models.CharField(max_length=20, choices=olla_choices, null=True)
    panuelo_choices = [(u'produces', u'produces')]
    item_panuelo = models.CharField(max_length=20, choices=panuelo_choices, null=True)
    papel_choices = [(u'produces', u'produces')]
    item_papel = models.CharField(max_length=20, choices=papel_choices, null=True)
    pastdnte_choices = [(u'produces', u'produces')]
    item_pastdnte = models.CharField(max_length=20, choices=pastdnte_choices, null=True)
    peine_choices = [(u'produces', u'produces')]
    item_peine = models.CharField(max_length=20, choices=peine_choices, null=True)
    peridco_choices = [(u'produces', u'produces')]
    item_peridco = models.CharField(max_length=20, choices=peridco_choices, null=True)
    plancha_choices = [(u'produces', u'produces')]
    item_plancha = models.CharField(max_length=20, choices=plancha_choices, null=True)
    plato_choices = [(u'produces', u'produces')]
    item_plato = models.CharField(max_length=20, choices=plato_choices, null=True)
    radio_choices = [(u'produces', u'produces')]
    item_radio = models.CharField(max_length=20, choices=radio_choices, null=True)
    reloj_choices = [(u'produces', u'produces')]
    item_reloj = models.CharField(max_length=20, choices=reloj_choices, null=True)
    servleta_choices = [(u'produces', u'produces')]
    item_servleta = models.CharField(max_length=20, choices=servleta_choices, null=True)
    tapete_choices = [(u'produces', u'produces')]
    item_tapete = models.CharField(max_length=20, choices=tapete_choices, null=True)
    taza_choices = [(u'produces', u'produces')]
    item_taza = models.CharField(max_length=20, choices=taza_choices, null=True)
    telefono_choices = [(u'produces', u'produces')]
    item_telefono = models.CharField(max_length=20, choices=telefono_choices, null=True)
    tenedor_choices = [(u'produces', u'produces')]
    item_tenedor = models.CharField(max_length=20, choices=tenedor_choices, null=True)
    tijeras_choices = [(u'produces', u'produces')]
    item_tijeras = models.CharField(max_length=20, choices=tijeras_choices, null=True)
    toalla_choices = [(u'produces', u'produces')]
    item_toalla = models.CharField(max_length=20, choices=toalla_choices, null=True)
    trapo_choices = [(u'produces', u'produces')]
    item_trapo = models.CharField(max_length=20, choices=trapo_choices, null=True)
    vasos_choices = [(u'produces', u'produces')]
    item_vasos = models.CharField(max_length=20, choices=vasos_choices, null=True)
    vela_choices = [(u'produces', u'produces')]
    item_vela = models.CharField(max_length=20, choices=vela_choices, null=True)
    albrpisc_choices = [(u'produces', u'produces')]
    item_albrpisc = models.CharField(max_length=20, choices=albrpisc_choices, null=True)
    arbol_choices = [(u'produces', u'produces')]
    item_arbol = models.CharField(max_length=20, choices=arbol_choices, null=True)
    bandera_choices = [(u'produces', u'produces')]
    item_bandera = models.CharField(max_length=20, choices=bandera_choices, null=True)
    cielo_choices = [(u'produces', u'produces')]
    item_cielo = models.CharField(max_length=20, choices=cielo_choices, null=True)
    coldera_choices = [(u'produces', u'produces')]
    item_coldera = models.CharField(max_length=20, choices=coldera_choices, null=True)
    columpio_choices = [(u'produces', u'produces')]
    item_columpio = models.CharField(max_length=20, choices=columpio_choices, null=True)
    estrella_choices = [(u'produces', u'produces')]
    item_estrella = models.CharField(max_length=20, choices=estrella_choices, null=True)
    flor_choices = [(u'produces', u'produces')]
    item_flor = models.CharField(max_length=20, choices=flor_choices, null=True)
    fuego_choices = [(u'produces', u'produces')]
    item_fuego = models.CharField(max_length=20, choices=fuego_choices, null=True)
    hojas_choices = [(u'produces', u'produces')]
    item_hojas = models.CharField(max_length=20, choices=hojas_choices, null=True)
    lena_choices = [(u'produces', u'produces')]
    item_lena = models.CharField(max_length=20, choices=lena_choices, null=True)
    lluvia_choices = [(u'produces', u'produces')]
    item_lluvia = models.CharField(max_length=20, choices=lluvia_choices, null=True)
    luna_choices = [(u'produces', u'produces')]
    item_luna = models.CharField(max_length=20, choices=luna_choices, null=True)
    maceta_choices = [(u'produces', u'produces')]
    item_maceta = models.CharField(max_length=20, choices=maceta_choices, null=True)
    manguera_choices = [(u'produces', u'produces')]
    item_manguera = models.CharField(max_length=20, choices=manguera_choices, null=True)
    muncniev_choices = [(u'produces', u'produces')]
    item_muncniev = models.CharField(max_length=20, choices=muncniev_choices, null=True)
    nieve_choices = [(u'produces', u'produces')]
    item_nieve = models.CharField(max_length=20, choices=nieve_choices, null=True)
    nube_choices = [(u'produces', u'produces')]
    item_nube = models.CharField(max_length=20, choices=nube_choices, null=True)
    pala_choices = [(u'produces', u'produces')]
    item_pala = models.CharField(max_length=20, choices=pala_choices, null=True)
    palo_choices = [(u'produces', u'produces')]
    item_palo = models.CharField(max_length=20, choices=palo_choices, null=True)
    pasto_choices = [(u'produces', u'produces')]
    item_pasto = models.CharField(max_length=20, choices=pasto_choices, null=True)
    piedra_choices = [(u'produces', u'produces')]
    item_piedra = models.CharField(max_length=20, choices=piedra_choices, null=True)
    planta_choices = [(u'produces', u'produces')]
    item_planta = models.CharField(max_length=20, choices=planta_choices, null=True)
    reja_choices = [(u'produces', u'produces')]
    item_reja = models.CharField(max_length=20, choices=reja_choices, null=True)
    resbadla_choices = [(u'produces', u'produces')]
    item_resbadla = models.CharField(max_length=20, choices=resbadla_choices, null=True)
    sol_choices = [(u'produces', u'produces')]
    item_sol = models.CharField(max_length=20, choices=sol_choices, null=True)
    tanque_choices = [(u'produces', u'produces')]
    item_tanque = models.CharField(max_length=20, choices=tanque_choices, null=True)
    techo_choices = [(u'produces', u'produces')]
    item_techo = models.CharField(max_length=20, choices=techo_choices, null=True)
    tierra_choices = [(u'produces', u'produces')]
    item_tierra = models.CharField(max_length=20, choices=tierra_choices, null=True)
    timbre_choices = [(u'produces', u'produces')]
    item_timbre = models.CharField(max_length=20, choices=timbre_choices, null=True)
    vientair_choices = [(u'produces', u'produces')]
    item_vientair = models.CharField(max_length=20, choices=vientair_choices, null=True)
    bacinica_choices = [(u'produces', u'produces')]
    item_bacinica = models.CharField(max_length=20, choices=bacinica_choices, null=True)
    banco1_choices = [(u'produces', u'produces')]
    item_banco1 = models.CharField(max_length=20, choices=banco1_choices, null=True)
    bano_choices = [(u'produces', u'produces')]
    item_bano = models.CharField(max_length=20, choices=bano_choices, null=True)
    cajon_choices = [(u'produces', u'produces')]
    item_cajon = models.CharField(max_length=20, choices=cajon_choices, null=True)
    cama_choices = [(u'produces', u'produces')]
    item_cama = models.CharField(max_length=20, choices=cama_choices, null=True)
    champu_choices = [(u'produces', u'produces')]
    item_champu = models.CharField(max_length=20, choices=champu_choices, null=True)
    cochera_choices = [(u'produces', u'produces')]
    item_cochera = models.CharField(max_length=20, choices=cochera_choices, null=True)
    cocina_choices = [(u'produces', u'produces')]
    item_cocina = models.CharField(max_length=20, choices=cocina_choices, null=True)
    comptdra_choices = [(u'produces', u'produces')]
    item_comptdra = models.CharField(max_length=20, choices=comptdra_choices, null=True)
    cuarto_choices = [(u'produces', u'produces')]
    item_cuarto = models.CharField(max_length=20, choices=cuarto_choices, null=True)
    cuna_choices = [(u'produces', u'produces')]
    item_cuna = models.CharField(max_length=20, choices=cuna_choices, null=True)
    escalera_choices = [(u'produces', u'produces')]
    item_escalera = models.CharField(max_length=20, choices=escalera_choices, null=True)
    estufa_choices = [(u'produces', u'produces')]
    item_estufa = models.CharField(max_length=20, choices=estufa_choices, null=True)
    horno_choices = [(u'produces', u'produces')]
    item_horno = models.CharField(max_length=20, choices=horno_choices, null=True)
    lavabo_choices = [(u'produces', u'produces')]
    item_lavabo = models.CharField(max_length=20, choices=lavabo_choices, null=True)
    lavadora_choices = [(u'produces', u'produces')]
    item_lavadora = models.CharField(max_length=20, choices=lavadora_choices, null=True)
    librero_choices = [(u'produces', u'produces')]
    item_librero = models.CharField(max_length=20, choices=librero_choices, null=True)
    mesa_choices = [(u'produces', u'produces')]
    item_mesa = models.CharField(max_length=20, choices=mesa_choices, null=True)
    mueble_choices = [(u'produces', u'produces')]
    item_mueble = models.CharField(max_length=20, choices=mueble_choices, null=True)
    patio1_choices = [(u'produces', u'produces')]
    item_patio1 = models.CharField(max_length=20, choices=patio1_choices, null=True)
    puerta_choices = [(u'produces', u'produces')]
    item_puerta = models.CharField(max_length=20, choices=puerta_choices, null=True)
    recamara_choices = [(u'produces', u'produces')]
    item_recamara = models.CharField(max_length=20, choices=recamara_choices, null=True)
    refrgrdr_choices = [(u'produces', u'produces')]
    item_refrgrdr = models.CharField(max_length=20, choices=refrgrdr_choices, null=True)
    regadera_choices = [(u'produces', u'produces')]
    item_regadera = models.CharField(max_length=20, choices=regadera_choices, null=True)
    ropero_choices = [(u'produces', u'produces')]
    item_ropero = models.CharField(max_length=20, choices=ropero_choices, null=True)
    sala_choices = [(u'produces', u'produces')]
    item_sala = models.CharField(max_length=20, choices=sala_choices, null=True)
    secadora_choices = [(u'produces', u'produces')]
    item_secadora = models.CharField(max_length=20, choices=secadora_choices, null=True)
    silla_choices = [(u'produces', u'produces')]
    item_silla = models.CharField(max_length=20, choices=silla_choices, null=True)
    sillon_choices = [(u'produces', u'produces')]
    item_sillon = models.CharField(max_length=20, choices=sillon_choices, null=True)
    sofa_choices = [(u'produces', u'produces')]
    item_sofa = models.CharField(max_length=20, choices=sofa_choices, null=True)
    televisn_choices = [(u'produces', u'produces')]
    item_televisn = models.CharField(max_length=20, choices=televisn_choices, null=True)
    tina_choices = [(u'produces', u'produces')]
    item_tina = models.CharField(max_length=20, choices=tina_choices, null=True)
    ventana_choices = [(u'produces', u'produces')]
    item_ventana = models.CharField(max_length=20, choices=ventana_choices, null=True)
    banco2_choices = [(u'produces', u'produces')]
    item_banco2 = models.CharField(max_length=20, choices=banco2_choices, null=True)
    bosque_choices = [(u'produces', u'produces')]
    item_bosque = models.CharField(max_length=20, choices=bosque_choices, null=True)
    calle_choices = [(u'produces', u'produces')]
    item_calle = models.CharField(max_length=20, choices=calle_choices, null=True)
    campo_choices = [(u'produces', u'produces')]
    item_campo = models.CharField(max_length=20, choices=campo_choices, null=True)
    casa_choices = [(u'produces', u'produces')]
    item_casa = models.CharField(max_length=20, choices=casa_choices, null=True)
    cerro_choices = [(u'produces', u'produces')]
    item_cerro = models.CharField(max_length=20, choices=cerro_choices, null=True)
    cine_choices = [(u'produces', u'produces')]
    item_cine = models.CharField(max_length=20, choices=cine_choices, null=True)
    circo_choices = [(u'produces', u'produces')]
    item_circo = models.CharField(max_length=20, choices=circo_choices, null=True)
    escuela_choices = [(u'produces', u'produces')]
    item_escuela = models.CharField(max_length=20, choices=escuela_choices, null=True)
    fabrica_choices = [(u'produces', u'produces')]
    item_fabrica = models.CharField(max_length=20, choices=fabrica_choices, null=True)
    fiesta_choices = [(u'produces', u'produces')]
    item_fiesta = models.CharField(max_length=20, choices=fiesta_choices, null=True)
    hospitl_choices = [(u'produces', u'produces')]
    item_hospitl = models.CharField(max_length=20, choices=hospitl_choices, null=True)
    iglstmpl_choices = [(u'produces', u'produces')]
    item_iglstmpl = models.CharField(max_length=20, choices=iglstmpl_choices, null=True)
    jardin_choices = [(u'produces', u'produces')]
    item_jardin = models.CharField(max_length=20, choices=jardin_choices, null=True)
    oficina_choices = [(u'produces', u'produces')]
    item_oficina = models.CharField(max_length=20, choices=oficina_choices, null=True)
    parque_choices = [(u'produces', u'produces')]
    item_parque = models.CharField(max_length=20, choices=parque_choices, null=True)
    patio2_choices = [(u'produces', u'produces')]
    item_patio2 = models.CharField(max_length=20, choices=patio2_choices, null=True)
    playa_choices = [(u'produces', u'produces')]
    item_playa = models.CharField(max_length=20, choices=playa_choices, null=True)
    rancho_choices = [(u'produces', u'produces')]
    item_rancho = models.CharField(max_length=20, choices=rancho_choices, null=True)
    rio_choices = [(u'produces', u'produces')]
    item_rio = models.CharField(max_length=20, choices=rio_choices, null=True)
    tienmerc_choices = [(u'produces', u'produces')]
    item_tienmerc = models.CharField(max_length=20, choices=tienmerc_choices, null=True)
    zoologic_choices = [(u'produces', u'produces')]
    item_zoologic = models.CharField(max_length=20, choices=zoologic_choices, null=True)
    abuela_choices = [(u'produces', u'produces')]
    item_abuela = models.CharField(max_length=20, choices=abuela_choices, null=True)
    abuelo_choices = [(u'produces', u'produces')]
    item_abuelo = models.CharField(max_length=20, choices=abuelo_choices, null=True)
    amiga_choices = [(u'produces', u'produces')]
    item_amiga = models.CharField(max_length=20, choices=amiga_choices, null=True)
    amigo_choices = [(u'produces', u'produces')]
    item_amigo = models.CharField(max_length=20, choices=amigo_choices, null=True)
    bebe_choices = [(u'produces', u'produces')]
    item_bebe = models.CharField(max_length=20, choices=bebe_choices, null=True)
    cura_choices = [(u'produces', u'produces')]
    item_cura = models.CharField(max_length=20, choices=cura_choices, null=True)
    doctor_choices = [(u'produces', u'produces')]
    item_doctor = models.CharField(max_length=20, choices=doctor_choices, null=True)
    enfermer_choices = [(u'produces', u'produces')]
    item_enfermer = models.CharField(max_length=20, choices=enfermer_choices, null=True)
    familia_choices = [(u'produces', u'produces')]
    item_familia = models.CharField(max_length=20, choices=familia_choices, null=True)
    hermana_choices = [(u'produces', u'produces')]
    item_hermana = models.CharField(max_length=20, choices=hermana_choices, null=True)
    hermano_choices = [(u'produces', u'produces')]
    item_hermano = models.CharField(max_length=20, choices=hermano_choices, null=True)
    madrina_choices = [(u'produces', u'produces')]
    item_madrina = models.CharField(max_length=20, choices=madrina_choices, null=True)
    maestra_choices = [(u'produces', u'produces')]
    item_maestra = models.CharField(max_length=20, choices=maestra_choices, null=True)
    mama_choices = [(u'produces', u'produces')]
    item_mama = models.CharField(max_length=20, choices=mama_choices, null=True)
    nana_choices = [(u'produces', u'produces')]
    item_nana = models.CharField(max_length=20, choices=nana_choices, null=True)
    nina_choices = [(u'produces', u'produces')]
    item_nina = models.CharField(max_length=20, choices=nina_choices, null=True)
    nino_choices = [(u'produces', u'produces')]
    item_nino = models.CharField(max_length=20, choices=nino_choices, null=True)
    nombrnin_choices = [(u'produces', u'produces')]
    item_nombrnin = models.CharField(max_length=20, choices=nombrnin_choices, null=True)
    padrino_choices = [(u'produces', u'produces')]
    item_padrino = models.CharField(max_length=20, choices=padrino_choices, null=True)
    papa_choices = [(u'produces', u'produces')]
    item_papa = models.CharField(max_length=20, choices=papa_choices, null=True)
    payaso_choices = [(u'produces', u'produces')]
    item_payaso = models.CharField(max_length=20, choices=payaso_choices, null=True)
    persona_choices = [(u'produces', u'produces')]
    item_persona = models.CharField(max_length=20, choices=persona_choices, null=True)
    policia_choices = [(u'produces', u'produces')]
    item_policia = models.CharField(max_length=20, choices=policia_choices, null=True)
    prima_choices = [(u'produces', u'produces')]
    item_prima = models.CharField(max_length=20, choices=prima_choices, null=True)
    primo_choices = [(u'produces', u'produces')]
    item_primo = models.CharField(max_length=20, choices=primo_choices, null=True)
    senor_choices = [(u'produces', u'produces')]
    item_senor = models.CharField(max_length=20, choices=senor_choices, null=True)
    senora_choices = [(u'produces', u'produces')]
    item_senora = models.CharField(max_length=20, choices=senora_choices, null=True)
    tia_choices = [(u'produces', u'produces')]
    item_tia = models.CharField(max_length=20, choices=tia_choices, null=True)
    tio_choices = [(u'produces', u'produces')]
    item_tio = models.CharField(max_length=20, choices=tio_choices, null=True)
    acerrin_choices = [(u'produces', u'produces')]
    item_acerrin = models.CharField(max_length=20, choices=acerrin_choices, null=True)
    adiosbye_choices = [(u'produces', u'produces')]
    item_adiosbye = models.CharField(max_length=20, choices=adiosbye_choices, null=True)
    ahitevoy_choices = [(u'produces', u'produces')]
    item_ahitevoy = models.CharField(max_length=20, choices=ahitevoy_choices, null=True)
    alagapat_choices = [(u'produces', u'produces')]
    item_alagapat = models.CharField(max_length=20, choices=alagapat_choices, null=True)
    aver_choices = [(u'produces', u'produces')]
    item_aver = models.CharField(max_length=20, choices=aver_choices, null=True)
    besitos_choices = [(u'produces', u'produces')]
    item_besitos = models.CharField(max_length=20, choices=besitos_choices, null=True)
    bravo_choices = [(u'produces', u'produces')]
    item_bravo = models.CharField(max_length=20, choices=bravo_choices, null=True)
    buendias_choices = [(u'produces', u'produces')]
    item_buendias = models.CharField(max_length=20, choices=buendias_choices, null=True)
    buennoch_choices = [(u'produces', u'produces')]
    item_buennoch = models.CharField(max_length=20, choices=buennoch_choices, null=True)
    cosqlits_choices = [(u'produces', u'produces')]
    item_cosqlits = models.CharField(max_length=20, choices=cosqlits_choices, null=True)
    gracias_choices = [(u'produces', u'produces')]
    item_gracias = models.CharField(max_length=20, choices=gracias_choices, null=True)
    hola_choices = [(u'produces', u'produces')]
    item_hola = models.CharField(max_length=20, choices=hola_choices, null=True)
    manosarb_choices = [(u'produces', u'produces')]
    item_manosarb = models.CharField(max_length=20, choices=manosarb_choices, null=True)
    ojitos_choices = [(u'produces', u'produces')]
    item_ojitos = models.CharField(max_length=20, choices=ojitos_choices, null=True)
    okay_choices = [(u'produces', u'produces')]
    item_okay = models.CharField(max_length=20, choices=okay_choices, null=True)
    ponetata_choices = [(u'produces', u'produces')]
    item_ponetata = models.CharField(max_length=20, choices=ponetata_choices, null=True)
    porfavor_choices = [(u'produces', u'produces')]
    item_porfavor = models.CharField(max_length=20, choices=porfavor_choices, null=True)
    salud_choices = [(u'produces', u'produces')]
    item_salud = models.CharField(max_length=20, choices=salud_choices, null=True)
    shhh_choices = [(u'produces', u'produces')]
    item_shhh = models.CharField(max_length=20, choices=shhh_choices, null=True)
    siesta_choices = [(u'produces', u'produces')]
    item_siesta = models.CharField(max_length=20, choices=siesta_choices, null=True)
    tengmant_choices = [(u'produces', u'produces')]
    item_tengmant = models.CharField(max_length=20, choices=tengmant_choices, null=True)
    tevypagr_choices = [(u'produces', u'produces')]
    item_tevypagr = models.CharField(max_length=20, choices=tevypagr_choices, null=True)
    tortlita_choices = [(u'produces', u'produces')]
    item_tortlita = models.CharField(max_length=20, choices=tortlita_choices, null=True)
    unodstrs_choices = [(u'produces', u'produces')]
    item_unodstrs = models.CharField(max_length=20, choices=unodstrs_choices, null=True)
    vamonos_choices = [(u'produces', u'produces')]
    item_vamonos = models.CharField(max_length=20, choices=vamonos_choices, null=True)
    ir_choices = [(u'produces', u'produces')]
    item_ir = models.CharField(max_length=20, choices=ir_choices, null=True)
    jalar_choices = [(u'produces', u'produces')]
    item_jalar = models.CharField(max_length=20, choices=jalar_choices, null=True)
    jugar_choices = [(u'produces', u'produces')]
    item_jugar = models.CharField(max_length=20, choices=jugar_choices, null=True)
    juntar_choices = [(u'produces', u'produces')]
    item_juntar = models.CharField(max_length=20, choices=juntar_choices, null=True)
    lastimar_choices = [(u'produces', u'produces')]
    item_lastimar = models.CharField(max_length=20, choices=lastimar_choices, null=True)
    lavar_choices = [(u'produces', u'produces')]
    item_lavar = models.CharField(max_length=20, choices=lavar_choices, null=True)
    leer_choices = [(u'produces', u'produces')]
    item_leer = models.CharField(max_length=20, choices=leer_choices, null=True)
    levntar_choices = [(u'produces', u'produces')]
    item_levntar = models.CharField(max_length=20, choices=levntar_choices, null=True)
    llevar_choices = [(u'produces', u'produces')]
    item_llevar = models.CharField(max_length=20, choices=llevar_choices, null=True)
    llorar_choices = [(u'produces', u'produces')]
    item_llorar = models.CharField(max_length=20, choices=llorar_choices, null=True)
    llover_choices = [(u'produces', u'produces')]
    item_llover = models.CharField(max_length=20, choices=llover_choices, null=True)
    meterse_choices = [(u'produces', u'produces')]
    item_meterse = models.CharField(max_length=20, choices=meterse_choices, null=True)
    mirar_choices = [(u'produces', u'produces')]
    item_mirar = models.CharField(max_length=20, choices=mirar_choices, null=True)
    morder_choices = [(u'produces', u'produces')]
    item_morder = models.CharField(max_length=20, choices=morder_choices, null=True)
    nadar_choices = [(u'produces', u'produces')]
    item_nadar = models.CharField(max_length=20, choices=nadar_choices, null=True)
    oir_choices = [(u'produces', u'produces')]
    item_oir = models.CharField(max_length=20, choices=oir_choices, null=True)
    parar_choices = [(u'produces', u'produces')]
    item_parar = models.CharField(max_length=20, choices=parar_choices, null=True)
    patear_choices = [(u'produces', u'produces')]
    item_patear = models.CharField(max_length=20, choices=patear_choices, null=True)
    patinar_choices = [(u'produces', u'produces')]
    item_patinar = models.CharField(max_length=20, choices=patinar_choices, null=True)
    pegar_choices = [(u'produces', u'produces')]
    item_pegar = models.CharField(max_length=20, choices=pegar_choices, null=True)
    peinarse_choices = [(u'produces', u'produces')]
    item_peinarse = models.CharField(max_length=20, choices=peinarse_choices, null=True)
    pensar_choices = [(u'produces', u'produces')]
    item_pensar = models.CharField(max_length=20, choices=pensar_choices, null=True)
    perder_choices = [(u'produces', u'produces')]
    item_perder = models.CharField(max_length=20, choices=perder_choices, null=True)
    pintar_choices = [(u'produces', u'produces')]
    item_pintar = models.CharField(max_length=20, choices=pintar_choices, null=True)
    platicar_choices = [(u'produces', u'produces')]
    item_platicar = models.CharField(max_length=20, choices=platicar_choices, null=True)
    poder_choices = [(u'produces', u'produces')]
    item_poder = models.CharField(max_length=20, choices=poder_choices, null=True)
    poner_choices = [(u'produces', u'produces')]
    item_poner = models.CharField(max_length=20, choices=poner_choices, null=True)
    prender_choices = [(u'produces', u'produces')]
    item_prender = models.CharField(max_length=20, choices=prender_choices, null=True)
    quedar_choices = [(u'produces', u'produces')]
    item_quedar = models.CharField(max_length=20, choices=quedar_choices, null=True)
    quemar_choices = [(u'produces', u'produces')]
    item_quemar = models.CharField(max_length=20, choices=quemar_choices, null=True)
    querer_choices = [(u'produces', u'produces')]
    item_querer = models.CharField(max_length=20, choices=querer_choices, null=True)
    quitarse_choices = [(u'produces', u'produces')]
    item_quitarse = models.CharField(max_length=20, choices=quitarse_choices, null=True)
    regalar_choices = [(u'produces', u'produces')]
    item_regalar = models.CharField(max_length=20, choices=regalar_choices, null=True)
    romper_choices = [(u'produces', u'produces')]
    item_romper = models.CharField(max_length=20, choices=romper_choices, null=True)
    saber_choices = [(u'produces', u'produces')]
    item_saber = models.CharField(max_length=20, choices=saber_choices, null=True)
    sacar_choices = [(u'produces', u'produces')]
    item_sacar = models.CharField(max_length=20, choices=sacar_choices, null=True)
    salir_choices = [(u'produces', u'produces')]
    item_salir = models.CharField(max_length=20, choices=salir_choices, null=True)
    saltar_choices = [(u'produces', u'produces')]
    item_saltar = models.CharField(max_length=20, choices=saltar_choices, null=True)
    saludar_choices = [(u'produces', u'produces')]
    item_saludar = models.CharField(max_length=20, choices=saludar_choices, null=True)
    sentar_choices = [(u'produces', u'produces')]
    item_sentar = models.CharField(max_length=20, choices=sentar_choices, null=True)
    soplar_choices = [(u'produces', u'produces')]
    item_soplar = models.CharField(max_length=20, choices=soplar_choices, null=True)
    subir_choices = [(u'produces', u'produces')]
    item_subir = models.CharField(max_length=20, choices=subir_choices, null=True)
    tapar_choices = [(u'produces', u'produces')]
    item_tapar = models.CharField(max_length=20, choices=tapar_choices, null=True)
    tener_choices = [(u'produces', u'produces')]
    item_tener = models.CharField(max_length=20, choices=tener_choices, null=True)
    terminar_choices = [(u'produces', u'produces')]
    item_terminar = models.CharField(max_length=20, choices=terminar_choices, null=True)
    tirar_choices = [(u'produces', u'produces')]
    item_tirar = models.CharField(max_length=20, choices=tirar_choices, null=True)
    tocar_choices = [(u'produces', u'produces')]
    item_tocar = models.CharField(max_length=20, choices=tocar_choices, null=True)
    tomar_choices = [(u'produces', u'produces')]
    item_tomar = models.CharField(max_length=20, choices=tomar_choices, null=True)
    traer_choices = [(u'produces', u'produces')]
    item_traer = models.CharField(max_length=20, choices=traer_choices, null=True)
    venir_choices = [(u'produces', u'produces')]
    item_venir = models.CharField(max_length=20, choices=venir_choices, null=True)
    ver_choices = [(u'produces', u'produces')]
    item_ver = models.CharField(max_length=20, choices=ver_choices, null=True)
    acabarse_choices = [(u'produces', u'produces')]
    item_acabarse = models.CharField(max_length=20, choices=acabarse_choices, null=True)
    acompnar_choices = [(u'produces', u'produces')]
    item_acompnar = models.CharField(max_length=20, choices=acompnar_choices, null=True)
    acostar_choices = [(u'produces', u'produces')]
    item_acostar = models.CharField(max_length=20, choices=acostar_choices, null=True)
    agarrar_choices = [(u'produces', u'produces')]
    item_agarrar = models.CharField(max_length=20, choices=agarrar_choices, null=True)
    almorzar_choices = [(u'produces', u'produces')]
    item_almorzar = models.CharField(max_length=20, choices=almorzar_choices, null=True)
    amararse_choices = [(u'produces', u'produces')]
    item_amararse = models.CharField(max_length=20, choices=amararse_choices, null=True)
    andar_choices = [(u'produces', u'produces')]
    item_andar = models.CharField(max_length=20, choices=andar_choices, null=True)
    apagar_choices = [(u'produces', u'produces')]
    item_apagar = models.CharField(max_length=20, choices=apagar_choices, null=True)
    apurar_choices = [(u'produces', u'produces')]
    item_apurar = models.CharField(max_length=20, choices=apurar_choices, null=True)
    arreglar_choices = [(u'produces', u'produces')]
    item_arreglar = models.CharField(max_length=20, choices=arreglar_choices, null=True)
    asustar_choices = [(u'produces', u'produces')]
    item_asustar = models.CharField(max_length=20, choices=asustar_choices, null=True)
    aventar_choices = [(u'produces', u'produces')]
    item_aventar = models.CharField(max_length=20, choices=aventar_choices, null=True)
    ayudar_choices = [(u'produces', u'produces')]
    item_ayudar = models.CharField(max_length=20, choices=ayudar_choices, null=True)
    bailar_choices = [(u'produces', u'produces')]
    item_bailar = models.CharField(max_length=20, choices=bailar_choices, null=True)
    bajarse_choices = [(u'produces', u'produces')]
    item_bajarse = models.CharField(max_length=20, choices=bajarse_choices, null=True)
    barrer_choices = [(u'produces', u'produces')]
    item_barrer = models.CharField(max_length=20, choices=barrer_choices, null=True)
    besar_choices = [(u'produces', u'produces')]
    item_besar = models.CharField(max_length=20, choices=besar_choices, null=True)
    brincar_choices = [(u'produces', u'produces')]
    item_brincar = models.CharField(max_length=20, choices=brincar_choices, null=True)
    buscar_choices = [(u'produces', u'produces')]
    item_buscar = models.CharField(max_length=20, choices=buscar_choices, null=True)
    caber_choices = [(u'produces', u'produces')]
    item_caber = models.CharField(max_length=20, choices=caber_choices, null=True)
    caer_choices = [(u'produces', u'produces')]
    item_caer = models.CharField(max_length=20, choices=caer_choices, null=True)
    callarse_choices = [(u'produces', u'produces')]
    item_callarse = models.CharField(max_length=20, choices=callarse_choices, null=True)
    caminar_choices = [(u'produces', u'produces')]
    item_caminar = models.CharField(max_length=20, choices=caminar_choices, null=True)
    cantar_choices = [(u'produces', u'produces')]
    item_cantar = models.CharField(max_length=20, choices=cantar_choices, null=True)
    cargar_choices = [(u'produces', u'produces')]
    item_cargar = models.CharField(max_length=20, choices=cargar_choices, null=True)
    cenar_choices = [(u'produces', u'produces')]
    item_cenar = models.CharField(max_length=20, choices=cenar_choices, null=True)
    cerrar_choices = [(u'produces', u'produces')]
    item_cerrar = models.CharField(max_length=20, choices=cerrar_choices, null=True)
    cocinar_choices = [(u'produces', u'produces')]
    item_cocinar = models.CharField(max_length=20, choices=cocinar_choices, null=True)
    comer_choices = [(u'produces', u'produces')]
    item_comer = models.CharField(max_length=20, choices=comer_choices, null=True)
    comprar_choices = [(u'produces', u'produces')]
    item_comprar = models.CharField(max_length=20, choices=comprar_choices, null=True)
    correr_choices = [(u'produces', u'produces')]
    item_correr = models.CharField(max_length=20, choices=correr_choices, null=True)
    cortar_choices = [(u'produces', u'produces')]
    item_cortar = models.CharField(max_length=20, choices=cortar_choices, null=True)
    dar_choices = [(u'produces', u'produces')]
    item_dar = models.CharField(max_length=20, choices=dar_choices, null=True)
    decir_choices = [(u'produces', u'produces')]
    item_decir = models.CharField(max_length=20, choices=decir_choices, null=True)
    desyunar_choices = [(u'produces', u'produces')]
    item_desyunar = models.CharField(max_length=20, choices=desyunar_choices, null=True)
    dibujar_choices = [(u'produces', u'produces')]
    item_dibujar = models.CharField(max_length=20, choices=dibujar_choices, null=True)
    doler_choices = [(u'produces', u'produces')]
    item_doler = models.CharField(max_length=20, choices=doler_choices, null=True)
    dormir_choices = [(u'produces', u'produces')]
    item_dormir = models.CharField(max_length=20, choices=dormir_choices, null=True)
    empujar_choices = [(u'produces', u'produces')]
    item_empujar = models.CharField(max_length=20, choices=empujar_choices, null=True)
    encontra_choices = [(u'produces', u'produces')]
    item_encontra = models.CharField(max_length=20, choices=encontra_choices, null=True)
    ensenar_choices = [(u'produces', u'produces')]
    item_ensenar = models.CharField(max_length=20, choices=ensenar_choices, null=True)
    entrar_choices = [(u'produces', u'produces')]
    item_entrar = models.CharField(max_length=20, choices=entrar_choices, null=True)
    equvcar_choices = [(u'produces', u'produces')]
    item_equvcar = models.CharField(max_length=20, choices=equvcar_choices, null=True)
    esconder_choices = [(u'produces', u'produces')]
    item_esconder = models.CharField(max_length=20, choices=esconder_choices, null=True)
    escribir_choices = [(u'produces', u'produces')]
    item_escribir = models.CharField(max_length=20, choices=escribir_choices, null=True)
    escuchar_choices = [(u'produces', u'produces')]
    item_escuchar = models.CharField(max_length=20, choices=escuchar_choices, null=True)
    esperar_choices = [(u'produces', u'produces')]
    item_esperar = models.CharField(max_length=20, choices=esperar_choices, null=True)
    ganar_choices = [(u'produces', u'produces')]
    item_ganar = models.CharField(max_length=20, choices=ganar_choices, null=True)
    gritar_choices = [(u'produces', u'produces')]
    item_gritar = models.CharField(max_length=20, choices=gritar_choices, null=True)
    gustar_choices = [(u'produces', u'produces')]
    item_gustar = models.CharField(max_length=20, choices=gustar_choices, null=True)
    hacer_choices = [(u'produces', u'produces')]
    item_hacer = models.CharField(max_length=20, choices=hacer_choices, null=True)
    abrir_choices = [(u'produces', u'produces')]
    item_abrir = models.CharField(max_length=20, choices=abrir_choices, null=True)
    estar_choices = [(u'produces', u'produces')]
    item_estar = models.CharField(max_length=20, choices=estar_choices, null=True)
    habrhay_choices = [(u'produces', u'produces')]
    item_habrhay = models.CharField(max_length=20, choices=habrhay_choices, null=True)
    ser_choices = [(u'produces', u'produces')]
    item_ser = models.CharField(max_length=20, choices=ser_choices, null=True)
    alto_choices = [(u'produces', u'produces')]
    item_alto = models.CharField(max_length=20, choices=alto_choices, null=True)
    amarillo_choices = [(u'produces', u'produces')]
    item_amarillo = models.CharField(max_length=20, choices=amarillo_choices, null=True)
    azul_choices = [(u'produces', u'produces')]
    item_azul = models.CharField(max_length=20, choices=azul_choices, null=True)
    blanco_choices = [(u'produces', u'produces')]
    item_blanco = models.CharField(max_length=20, choices=blanco_choices, null=True)
    bonita_choices = [(u'produces', u'produces')]
    item_bonita = models.CharField(max_length=20, choices=bonita_choices, null=True)
    bueno_choices = [(u'produces', u'produces')]
    item_bueno = models.CharField(max_length=20, choices=bueno_choices, null=True)
    caliente_choices = [(u'produces', u'produces')]
    item_caliente = models.CharField(max_length=20, choices=caliente_choices, null=True)
    cansado_choices = [(u'produces', u'produces')]
    item_cansado = models.CharField(max_length=20, choices=cansado_choices, null=True)
    chaparo_choices = [(u'produces', u'produces')]
    item_chaparo = models.CharField(max_length=20, choices=chaparo_choices, null=True)
    chico_choices = [(u'produces', u'produces')]
    item_chico = models.CharField(max_length=20, choices=chico_choices, null=True)
    chulo_choices = [(u'produces', u'produces')]
    item_chulo = models.CharField(max_length=20, choices=chulo_choices, null=True)
    descompu_choices = [(u'produces', u'produces')]
    item_descompu = models.CharField(max_length=20, choices=descompu_choices, null=True)
    despiert_choices = [(u'produces', u'produces')]
    item_despiert = models.CharField(max_length=20, choices=despiert_choices, null=True)
    difernte_choices = [(u'produces', u'produces')]
    item_difernte = models.CharField(max_length=20, choices=difernte_choices, null=True)
    dificil_choices = [(u'produces', u'produces')]
    item_dificil = models.CharField(max_length=20, choices=dificil_choices, null=True)
    duro_choices = [(u'produces', u'produces')]
    item_duro = models.CharField(max_length=20, choices=duro_choices, null=True)
    enfermo_choices = [(u'produces', u'produces')]
    item_enfermo = models.CharField(max_length=20, choices=enfermo_choices, null=True)
    enojado_choices = [(u'produces', u'produces')]
    item_enojado = models.CharField(max_length=20, choices=enojado_choices, null=True)
    feliz_choices = [(u'produces', u'produces')]
    item_feliz = models.CharField(max_length=20, choices=feliz_choices, null=True)
    feo_choices = [(u'produces', u'produces')]
    item_feo = models.CharField(max_length=20, choices=feo_choices, null=True)
    flaco_choices = [(u'produces', u'produces')]
    item_flaco = models.CharField(max_length=20, choices=flaco_choices, null=True)
    frio_choices = [(u'produces', u'produces')]
    item_frio = models.CharField(max_length=20, choices=frio_choices, null=True)
    fuchi_choices = [(u'produces', u'produces')]
    item_fuchi = models.CharField(max_length=20, choices=fuchi_choices, null=True)
    fuerte_choices = [(u'produces', u'produces')]
    item_fuerte = models.CharField(max_length=20, choices=fuerte_choices, null=True)
    gordo_choices = [(u'produces', u'produces')]
    item_gordo = models.CharField(max_length=20, choices=gordo_choices, null=True)
    grande_choices = [(u'produces', u'produces')]
    item_grande = models.CharField(max_length=20, choices=grande_choices, null=True)
    guapo_choices = [(u'produces', u'produces')]
    item_guapo = models.CharField(max_length=20, choices=guapo_choices, null=True)
    hambre_choices = [(u'produces', u'produces')]
    item_hambre = models.CharField(max_length=20, choices=hambre_choices, null=True)
    igual_choices = [(u'produces', u'produces')]
    item_igual = models.CharField(max_length=20, choices=igual_choices, null=True)
    largo_choices = [(u'produces', u'produces')]
    item_largo = models.CharField(max_length=20, choices=largo_choices, null=True)
    lento_choices = [(u'produces', u'produces')]
    item_lento = models.CharField(max_length=20, choices=lento_choices, null=True)
    limpio_choices = [(u'produces', u'produces')]
    item_limpio = models.CharField(max_length=20, choices=limpio_choices, null=True)
    linda_choices = [(u'produces', u'produces')]
    item_linda = models.CharField(max_length=20, choices=linda_choices, null=True)
    lleno_choices = [(u'produces', u'produces')]
    item_lleno = models.CharField(max_length=20, choices=lleno_choices, null=True)
    malo_choices = [(u'produces', u'produces')]
    item_malo = models.CharField(max_length=20, choices=malo_choices, null=True)
    mejor_choices = [(u'produces', u'produces')]
    item_mejor = models.CharField(max_length=20, choices=mejor_choices, null=True)
    miedsust_choices = [(u'produces', u'produces')]
    item_miedsust = models.CharField(max_length=20, choices=miedsust_choices, null=True)
    mojado_choices = [(u'produces', u'produces')]
    item_mojado = models.CharField(max_length=20, choices=mojado_choices, null=True)
    morado_choices = [(u'produces', u'produces')]
    item_morado = models.CharField(max_length=20, choices=morado_choices, null=True)
    negro_choices = [(u'produces', u'produces')]
    item_negro = models.CharField(max_length=20, choices=negro_choices, null=True)
    nuevo_choices = [(u'produces', u'produces')]
    item_nuevo = models.CharField(max_length=20, choices=nuevo_choices, null=True)
    oscuro_choices = [(u'produces', u'produces')]
    item_oscuro = models.CharField(max_length=20, choices=oscuro_choices, null=True)
    pegajoso_choices = [(u'produces', u'produces')]
    item_pegajoso = models.CharField(max_length=20, choices=pegajoso_choices, null=True)
    pelgrso_choices = [(u'produces', u'produces')]
    item_pelgrso = models.CharField(max_length=20, choices=pelgrso_choices, null=True)
    pesado_choices = [(u'produces', u'produces')]
    item_pesado = models.CharField(max_length=20, choices=pesado_choices, null=True)
    pobre_choices = [(u'produces', u'produces')]
    item_pobre = models.CharField(max_length=20, choices=pobre_choices, null=True)
    primero_choices = [(u'produces', u'produces')]
    item_primero = models.CharField(max_length=20, choices=primero_choices, null=True)
    rapido1_choices = [(u'produces', u'produces')]
    item_rapido1 = models.CharField(max_length=20, choices=rapido1_choices, null=True)
    rojo_choices = [(u'produces', u'produces')]
    item_rojo = models.CharField(max_length=20, choices=rojo_choices, null=True)
    rosa_choices = [(u'produces', u'produces')]
    item_rosa = models.CharField(max_length=20, choices=rosa_choices, null=True)
    roto_choices = [(u'produces', u'produces')]
    item_roto = models.CharField(max_length=20, choices=roto_choices, null=True)
    ruidoso_choices = [(u'produces', u'produces')]
    item_ruidoso = models.CharField(max_length=20, choices=ruidoso_choices, null=True)
    seco_choices = [(u'produces', u'produces')]
    item_seco = models.CharField(max_length=20, choices=seco_choices, null=True)
    suave_choices = [(u'produces', u'produces')]
    item_suave = models.CharField(max_length=20, choices=suave_choices, null=True)
    sucio_choices = [(u'produces', u'produces')]
    item_sucio = models.CharField(max_length=20, choices=sucio_choices, null=True)
    tonto_choices = [(u'produces', u'produces')]
    item_tonto = models.CharField(max_length=20, choices=tonto_choices, null=True)
    tranquil_choices = [(u'produces', u'produces')]
    item_tranquil = models.CharField(max_length=20, choices=tranquil_choices, null=True)
    travieso_choices = [(u'produces', u'produces')]
    item_travieso = models.CharField(max_length=20, choices=travieso_choices, null=True)
    triste_choices = [(u'produces', u'produces')]
    item_triste = models.CharField(max_length=20, choices=triste_choices, null=True)
    ultimo_choices = [(u'produces', u'produces')]
    item_ultimo = models.CharField(max_length=20, choices=ultimo_choices, null=True)
    vacio_choices = [(u'produces', u'produces')]
    item_vacio = models.CharField(max_length=20, choices=vacio_choices, null=True)
    verde_choices = [(u'produces', u'produces')]
    item_verde = models.CharField(max_length=20, choices=verde_choices, null=True)
    viejo_choices = [(u'produces', u'produces')]
    item_viejo = models.CharField(max_length=20, choices=viejo_choices, null=True)
    ahorita_choices = [(u'produces', u'produces')]
    item_ahorita = models.CharField(max_length=20, choices=ahorita_choices, null=True)
    alrato_choices = [(u'produces', u'produces')]
    item_alrato = models.CharField(max_length=20, choices=alrato_choices, null=True)
    antes_choices = [(u'produces', u'produces')]
    item_antes = models.CharField(max_length=20, choices=antes_choices, null=True)
    ayer_choices = [(u'produces', u'produces')]
    item_ayer = models.CharField(max_length=20, choices=ayer_choices, null=True)
    despues_choices = [(u'produces', u'produces')]
    item_despues = models.CharField(max_length=20, choices=despues_choices, null=True)
    dia_choices = [(u'produces', u'produces')]
    item_dia = models.CharField(max_length=20, choices=dia_choices, null=True)
    enlamana_choices = [(u'produces', u'produces')]
    item_enlamana = models.CharField(max_length=20, choices=enlamana_choices, null=True)
    enlanoch_choices = [(u'produces', u'produces')]
    item_enlanoch = models.CharField(max_length=20, choices=enlanoch_choices, null=True)
    enlatard_choices = [(u'produces', u'produces')]
    item_enlatard = models.CharField(max_length=20, choices=enlatard_choices, null=True)
    hoy_choices = [(u'produces', u'produces')]
    item_hoy = models.CharField(max_length=20, choices=hoy_choices, null=True)
    manana_choices = [(u'produces', u'produces')]
    item_manana = models.CharField(max_length=20, choices=manana_choices, null=True)
    noche_choices = [(u'produces', u'produces')]
    item_noche = models.CharField(max_length=20, choices=noche_choices, null=True)
    aquel_choices = [(u'produces', u'produces')]
    item_aquel = models.CharField(max_length=20, choices=aquel_choices, null=True)
    aquela_choices = [(u'produces', u'produces')]
    item_aquela = models.CharField(max_length=20, choices=aquela_choices, null=True)
    aquelas_choices = [(u'produces', u'produces')]
    item_aquelas = models.CharField(max_length=20, choices=aquelas_choices, null=True)
    aquelos_choices = [(u'produces', u'produces')]
    item_aquelos = models.CharField(max_length=20, choices=aquelos_choices, null=True)
    el1_choices = [(u'produces', u'produces')]
    item_el1 = models.CharField(max_length=20, choices=el1_choices, null=True)
    ella_choices = [(u'produces', u'produces')]
    item_ella = models.CharField(max_length=20, choices=ella_choices, null=True)
    ellas_choices = [(u'produces', u'produces')]
    item_ellas = models.CharField(max_length=20, choices=ellas_choices, null=True)
    ellos_choices = [(u'produces', u'produces')]
    item_ellos = models.CharField(max_length=20, choices=ellos_choices, null=True)
    esa_choices = [(u'produces', u'produces')]
    item_esa = models.CharField(max_length=20, choices=esa_choices, null=True)
    esas_choices = [(u'produces', u'produces')]
    item_esas = models.CharField(max_length=20, choices=esas_choices, null=True)
    ese_choices = [(u'produces', u'produces')]
    item_ese = models.CharField(max_length=20, choices=ese_choices, null=True)
    eso_choices = [(u'produces', u'produces')]
    item_eso = models.CharField(max_length=20, choices=eso_choices, null=True)
    esos_choices = [(u'produces', u'produces')]
    item_esos = models.CharField(max_length=20, choices=esos_choices, null=True)
    esta_choices = [(u'produces', u'produces')]
    item_esta = models.CharField(max_length=20, choices=esta_choices, null=True)
    estas_choices = [(u'produces', u'produces')]
    item_estas = models.CharField(max_length=20, choices=estas_choices, null=True)
    este_choices = [(u'produces', u'produces')]
    item_este = models.CharField(max_length=20, choices=este_choices, null=True)
    esto_choices = [(u'produces', u'produces')]
    item_esto = models.CharField(max_length=20, choices=esto_choices, null=True)
    estos_choices = [(u'produces', u'produces')]
    item_estos = models.CharField(max_length=20, choices=estos_choices, null=True)
    prole_choices = [(u'produces', u'produces')]
    item_prole = models.CharField(max_length=20, choices=prole_choices, null=True)
    les_choices = [(u'produces', u'produces')]
    item_les = models.CharField(max_length=20, choices=les_choices, null=True)
    lo_choices = [(u'produces', u'produces')]
    item_lo = models.CharField(max_length=20, choices=lo_choices, null=True)
    me_choices = [(u'produces', u'produces')]
    item_me = models.CharField(max_length=20, choices=me_choices, null=True)
    mi_choices = [(u'produces', u'produces')]
    item_mi = models.CharField(max_length=20, choices=mi_choices, null=True)
    mia_choices = [(u'produces', u'produces')]
    item_mia = models.CharField(max_length=20, choices=mia_choices, null=True)
    mias_choices = [(u'produces', u'produces')]
    item_mias = models.CharField(max_length=20, choices=mias_choices, null=True)
    mio_choices = [(u'produces', u'produces')]
    item_mio = models.CharField(max_length=20, choices=mio_choices, null=True)
    mios_choices = [(u'produces', u'produces')]
    item_mios = models.CharField(max_length=20, choices=mios_choices, null=True)
    nosotros_choices = [(u'produces', u'produces')]
    item_nosotros = models.CharField(max_length=20, choices=nosotros_choices, null=True)
    nuestro_choices = [(u'produces', u'produces')]
    item_nuestro = models.CharField(max_length=20, choices=nuestro_choices, null=True)
    se_choices = [(u'produces', u'produces')]
    item_se = models.CharField(max_length=20, choices=se_choices, null=True)
    su_choices = [(u'produces', u'produces')]
    item_su = models.CharField(max_length=20, choices=su_choices, null=True)
    suya_choices = [(u'produces', u'produces')]
    item_suya = models.CharField(max_length=20, choices=suya_choices, null=True)
    suyas_choices = [(u'produces', u'produces')]
    item_suyas = models.CharField(max_length=20, choices=suyas_choices, null=True)
    suyo_choices = [(u'produces', u'produces')]
    item_suyo = models.CharField(max_length=20, choices=suyo_choices, null=True)
    suyos_choices = [(u'produces', u'produces')]
    item_suyos = models.CharField(max_length=20, choices=suyos_choices, null=True)
    te2_choices = [(u'produces', u'produces')]
    item_te2 = models.CharField(max_length=20, choices=te2_choices, null=True)
    ti_choices = [(u'produces', u'produces')]
    item_ti = models.CharField(max_length=20, choices=ti_choices, null=True)
    tu_choices = [(u'produces', u'produces')]
    item_tu = models.CharField(max_length=20, choices=tu_choices, null=True)
    tuya_choices = [(u'produces', u'produces')]
    item_tuya = models.CharField(max_length=20, choices=tuya_choices, null=True)
    tuyas_choices = [(u'produces', u'produces')]
    item_tuyas = models.CharField(max_length=20, choices=tuyas_choices, null=True)
    tuyo_choices = [(u'produces', u'produces')]
    item_tuyo = models.CharField(max_length=20, choices=tuyo_choices, null=True)
    tuyos_choices = [(u'produces', u'produces')]
    item_tuyos = models.CharField(max_length=20, choices=tuyos_choices, null=True)
    yo_choices = [(u'produces', u'produces')]
    item_yo = models.CharField(max_length=20, choices=yo_choices, null=True)
    como_choices = [(u'produces', u'produces')]
    item_como = models.CharField(max_length=20, choices=como_choices, null=True)
    cual_choices = [(u'produces', u'produces')]
    item_cual = models.CharField(max_length=20, choices=cual_choices, null=True)
    cuando_choices = [(u'produces', u'produces')]
    item_cuando = models.CharField(max_length=20, choices=cuando_choices, null=True)
    donde_choices = [(u'produces', u'produces')]
    item_donde = models.CharField(max_length=20, choices=donde_choices, null=True)
    porque_choices = [(u'produces', u'produces')]
    item_porque = models.CharField(max_length=20, choices=porque_choices, null=True)
    que1_choices = [(u'produces', u'produces')]
    item_que1 = models.CharField(max_length=20, choices=que1_choices, null=True)
    quien_choices = [(u'produces', u'produces')]
    item_quien = models.CharField(max_length=20, choices=quien_choices, null=True)
    a_choices = [(u'produces', u'produces')]
    item_a = models.CharField(max_length=20, choices=a_choices, null=True)
    con_choices = [(u'produces', u'produces')]
    item_con = models.CharField(max_length=20, choices=con_choices, null=True)
    de_choices = [(u'produces', u'produces')]
    item_de = models.CharField(max_length=20, choices=de_choices, null=True)
    el2_choices = [(u'produces', u'produces')]
    item_el2 = models.CharField(max_length=20, choices=el2_choices, null=True)
    en_choices = [(u'produces', u'produces')]
    item_en = models.CharField(max_length=20, choices=en_choices, null=True)
    entre_choices = [(u'produces', u'produces')]
    item_entre = models.CharField(max_length=20, choices=entre_choices, null=True)
    la_choices = [(u'produces', u'produces')]
    item_la = models.CharField(max_length=20, choices=la_choices, null=True)
    las_choices = [(u'produces', u'produces')]
    item_las = models.CharField(max_length=20, choices=las_choices, null=True)
    los_choices = [(u'produces', u'produces')]
    item_los = models.CharField(max_length=20, choices=los_choices, null=True)
    para_choices = [(u'produces', u'produces')]
    item_para = models.CharField(max_length=20, choices=para_choices, null=True)
    pero_choices = [(u'produces', u'produces')]
    item_pero = models.CharField(max_length=20, choices=pero_choices, null=True)
    un_choices = [(u'produces', u'produces')]
    item_un = models.CharField(max_length=20, choices=un_choices, null=True)
    una_choices = [(u'produces', u'produces')]
    item_una = models.CharField(max_length=20, choices=una_choices, null=True)
    unas_choices = [(u'produces', u'produces')]
    item_unas = models.CharField(max_length=20, choices=unas_choices, null=True)
    unos_choices = [(u'produces', u'produces')]
    item_unos = models.CharField(max_length=20, choices=unos_choices, null=True)
    asi_choices = [(u'produces', u'produces')]
    item_asi = models.CharField(max_length=20, choices=asi_choices, null=True)
    bien_choices = [(u'produces', u'produces')]
    item_bien = models.CharField(max_length=20, choices=bien_choices, null=True)
    despacio_choices = [(u'produces', u'produces')]
    item_despacio = models.CharField(max_length=20, choices=despacio_choices, null=True)
    mal_choices = [(u'produces', u'produces')]
    item_mal = models.CharField(max_length=20, choices=mal_choices, null=True)
    mas_choices = [(u'produces', u'produces')]
    item_mas = models.CharField(max_length=20, choices=mas_choices, null=True)
    mucho_choices = [(u'produces', u'produces')]
    item_mucho = models.CharField(max_length=20, choices=mucho_choices, null=True)
    nada_choices = [(u'produces', u'produces')]
    item_nada = models.CharField(max_length=20, choices=nada_choices, null=True)
    no_choices = [(u'produces', u'produces')]
    item_no = models.CharField(max_length=20, choices=no_choices, null=True)
    nohay_choices = [(u'produces', u'produces')]
    item_nohay = models.CharField(max_length=20, choices=nohay_choices, null=True)
    otravez_choices = [(u'produces', u'produces')]
    item_otravez = models.CharField(max_length=20, choices=otravez_choices, null=True)
    pocquito_choices = [(u'produces', u'produces')]
    item_pocquito = models.CharField(max_length=20, choices=pocquito_choices, null=True)
    rapido2_choices = [(u'produces', u'produces')]
    item_rapido2 = models.CharField(max_length=20, choices=rapido2_choices, null=True)
    si_choices = [(u'produces', u'produces')]
    item_si = models.CharField(max_length=20, choices=si_choices, null=True)
    todo_choices = [(u'produces', u'produces')]
    item_todo = models.CharField(max_length=20, choices=todo_choices, null=True)
    ya_choices = [(u'produces', u'produces')]
    item_ya = models.CharField(max_length=20, choices=ya_choices, null=True)
    abajo_choices = [(u'produces', u'produces')]
    item_abajo = models.CharField(max_length=20, choices=abajo_choices, null=True)
    adentro_choices = [(u'produces', u'produces')]
    item_adentro = models.CharField(max_length=20, choices=adentro_choices, null=True)
    afuera_choices = [(u'produces', u'produces')]
    item_afuera = models.CharField(max_length=20, choices=afuera_choices, null=True)
    ahi_choices = [(u'produces', u'produces')]
    item_ahi = models.CharField(max_length=20, choices=ahi_choices, null=True)
    alla_choices = [(u'produces', u'produces')]
    item_alla = models.CharField(max_length=20, choices=alla_choices, null=True)
    alli_choices = [(u'produces', u'produces')]
    item_alli = models.CharField(max_length=20, choices=alli_choices, null=True)
    aqui_choices = [(u'produces', u'produces')]
    item_aqui = models.CharField(max_length=20, choices=aqui_choices, null=True)
    arriba_choices = [(u'produces', u'produces')]
    item_arriba = models.CharField(max_length=20, choices=arriba_choices, null=True)
    atras_choices = [(u'produces', u'produces')]
    item_atras = models.CharField(max_length=20, choices=atras_choices, null=True)
    cerca_choices = [(u'produces', u'produces')]
    item_cerca = models.CharField(max_length=20, choices=cerca_choices, null=True)
    encima_choices = [(u'produces', u'produces')]
    item_encima = models.CharField(max_length=20, choices=encima_choices, null=True)
    enfrente_choices = [(u'produces', u'produces')]
    item_enfrente = models.CharField(max_length=20, choices=enfrente_choices, null=True)
    lejos_choices = [(u'produces', u'produces')]
    item_lejos = models.CharField(max_length=20, choices=lejos_choices, null=True)
    entonces_choices = [(u'produces', u'produces')]
    item_entonces = models.CharField(max_length=20, choices=entonces_choices, null=True)
    luego_choices = [(u'produces', u'produces')]
    item_luego = models.CharField(max_length=20, choices=luego_choices, null=True)
    o_choices = [(u'produces', u'produces')]
    item_o = models.CharField(max_length=20, choices=o_choices, null=True)
    pues_choices = [(u'produces', u'produces')]
    item_pues = models.CharField(max_length=20, choices=pues_choices, null=True)
    que2_choices = [(u'produces', u'produces')]
    item_que2 = models.CharField(max_length=20, choices=que2_choices, null=True)
    y_choices = [(u'produces', u'produces')]
    item_y = models.CharField(max_length=20, choices=y_choices, null=True)


class Spanish_WG(BaseTable):
    am_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_am = models.CharField(max_length=20, choices=am_choices, null=True)
    ay_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_ay = models.CharField(max_length=20, choices=ay_choices, null=True)
    beemee_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_beemee = models.CharField(max_length=20, choices=beemee_choices, null=True)
    cuacua_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cuacua = models.CharField(max_length=20, choices=cuacua_choices, null=True)
    guagua_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_guagua = models.CharField(max_length=20, choices=guagua_choices, null=True)
    miau_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_miau = models.CharField(max_length=20, choices=miau_choices, null=True)
    muu_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_muu = models.CharField(max_length=20, choices=muu_choices, null=True)
    piopio_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_piopio = models.CharField(max_length=20, choices=piopio_choices, null=True)
    pipi_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_pipi = models.CharField(max_length=20, choices=pipi_choices, null=True)
    pum_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_pum = models.CharField(max_length=20, choices=pum_choices, null=True)
    qiqiriq_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_qiqiriq = models.CharField(max_length=20, choices=qiqiriq_choices, null=True)
    tutu_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_tutu = models.CharField(max_length=20, choices=tutu_choices, null=True)
    abeja_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_abeja = models.CharField(max_length=20, choices=abeja_choices, null=True)
    animal_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_animal = models.CharField(max_length=20, choices=animal_choices, null=True)
    arana_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_arana = models.CharField(max_length=20, choices=arana_choices, null=True)
    ardilla_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_ardilla = models.CharField(max_length=20, choices=ardilla_choices, null=True)
    borrego_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_borrego = models.CharField(max_length=20, choices=borrego_choices, null=True)
    buho_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_buho = models.CharField(max_length=20, choices=buho_choices, null=True)
    burro_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_burro = models.CharField(max_length=20, choices=burro_choices, null=True)
    caballo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_caballo = models.CharField(max_length=20, choices=caballo_choices, null=True)
    cabra_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cabra = models.CharField(max_length=20, choices=cabra_choices, null=True)
    conejo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_conejo = models.CharField(max_length=20, choices=conejo_choices, null=True)
    elefant_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_elefant = models.CharField(max_length=20, choices=elefant_choices, null=True)
    gallina_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_gallina = models.CharField(max_length=20, choices=gallina_choices, null=True)
    gato_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_gato = models.CharField(max_length=20, choices=gato_choices, null=True)
    guajolo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_guajolo = models.CharField(max_length=20, choices=guajolo_choices, null=True)
    hippotm_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_hippotm = models.CharField(max_length=20, choices=hippotm_choices, null=True)
    hormiga_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_hormiga = models.CharField(max_length=20, choices=hormiga_choices, null=True)
    jirafa_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_jirafa = models.CharField(max_length=20, choices=jirafa_choices, null=True)
    leon_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_leon = models.CharField(max_length=20, choices=leon_choices, null=True)
    lobo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_lobo = models.CharField(max_length=20, choices=lobo_choices, null=True)
    maripos_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_maripos = models.CharField(max_length=20, choices=maripos_choices, null=True)
    mono_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_mono = models.CharField(max_length=20, choices=mono_choices, null=True)
    mosca_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_mosca = models.CharField(max_length=20, choices=mosca_choices, null=True)
    oso_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_oso = models.CharField(max_length=20, choices=oso_choices, null=True)
    pajaro_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_pajaro = models.CharField(max_length=20, choices=pajaro_choices, null=True)
    pato_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_pato = models.CharField(max_length=20, choices=pato_choices, null=True)
    perro_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_perro = models.CharField(max_length=20, choices=perro_choices, null=True)
    pescado_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_pescado = models.CharField(max_length=20, choices=pescado_choices, null=True)
    pinguin_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_pinguin = models.CharField(max_length=20, choices=pinguin_choices, null=True)
    pollito_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_pollito = models.CharField(max_length=20, choices=pollito_choices, null=True)
    puerco_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_puerco = models.CharField(max_length=20, choices=puerco_choices, null=True)
    rana_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_rana = models.CharField(max_length=20, choices=rana_choices, null=True)
    raton_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_raton = models.CharField(max_length=20, choices=raton_choices, null=True)
    tigre_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_tigre = models.CharField(max_length=20, choices=tigre_choices, null=True)
    tortuga_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_tortuga = models.CharField(max_length=20, choices=tortuga_choices, null=True)
    vaca_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_vaca = models.CharField(max_length=20, choices=vaca_choices, null=True)
    venado_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_venado = models.CharField(max_length=20, choices=venado_choices, null=True)
    avion_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_avion = models.CharField(max_length=20, choices=avion_choices, null=True)
    barco_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_barco = models.CharField(max_length=20, choices=barco_choices, null=True)
    bicicle_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_bicicle = models.CharField(max_length=20, choices=bicicle_choices, null=True)
    camibom_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_camibom = models.CharField(max_length=20, choices=camibom_choices, null=True)
    camion_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_camion = models.CharField(max_length=20, choices=camion_choices, null=True)
    carreol_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_carreol = models.CharField(max_length=20, choices=carreol_choices, null=True)
    carro_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_carro = models.CharField(max_length=20, choices=carro_choices, null=True)
    moto_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_moto = models.CharField(max_length=20, choices=moto_choices, null=True)
    tren_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_tren = models.CharField(max_length=20, choices=tren_choices, null=True)
    agua_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_agua = models.CharField(max_length=20, choices=agua_choices, null=True)
    arroz_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_arroz = models.CharField(max_length=20, choices=arroz_choices, null=True)
    atole_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_atole = models.CharField(max_length=20, choices=atole_choices, null=True)
    cafe_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cafe = models.CharField(max_length=20, choices=cafe_choices, null=True)
    carne_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_carne = models.CharField(max_length=20, choices=carne_choices, null=True)
    cereal_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cereal = models.CharField(max_length=20, choices=cereal_choices, null=True)
    chile_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_chile = models.CharField(max_length=20, choices=chile_choices, null=True)
    comida_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_comida = models.CharField(max_length=20, choices=comida_choices, null=True)
    dulce_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_dulce = models.CharField(max_length=20, choices=dulce_choices, null=True)
    frijole_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_frijole = models.CharField(max_length=20, choices=frijole_choices, null=True)
    galleta_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_galleta = models.CharField(max_length=20, choices=galleta_choices, null=True)
    helado_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_helado = models.CharField(max_length=20, choices=helado_choices, null=True)
    huevo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_huevo = models.CharField(max_length=20, choices=huevo_choices, null=True)
    jamon_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_jamon = models.CharField(max_length=20, choices=jamon_choices, null=True)
    jugo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_jugo = models.CharField(max_length=20, choices=jugo_choices, null=True)
    leche_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_leche = models.CharField(max_length=20, choices=leche_choices, null=True)
    manzana_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_manzana = models.CharField(max_length=20, choices=manzana_choices, null=True)
    naranja_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_naranja = models.CharField(max_length=20, choices=naranja_choices, null=True)
    paleta_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_paleta = models.CharField(max_length=20, choices=paleta_choices, null=True)
    pan_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_pan = models.CharField(max_length=20, choices=pan_choices, null=True)
    pastel_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_pastel = models.CharField(max_length=20, choices=pastel_choices, null=True)
    platano_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_platano = models.CharField(max_length=20, choices=platano_choices, null=True)
    pollo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_pollo = models.CharField(max_length=20, choices=pollo_choices, null=True)
    quesdil_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_quesdil = models.CharField(max_length=20, choices=quesdil_choices, null=True)
    queso_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_queso = models.CharField(max_length=20, choices=queso_choices, null=True)
    salchch_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_salchch = models.CharField(max_length=20, choices=salchch_choices, null=True)
    soda_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_soda = models.CharField(max_length=20, choices=soda_choices, null=True)
    sopa_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_sopa = models.CharField(max_length=20, choices=sopa_choices, null=True)
    tortila_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_tortila = models.CharField(max_length=20, choices=tortila_choices, null=True)
    uvas_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_uvas = models.CharField(max_length=20, choices=uvas_choices, null=True)
    aretes_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_aretes = models.CharField(max_length=20, choices=aretes_choices, null=True)
    babera_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_babera = models.CharField(max_length=20, choices=babera_choices, null=True)
    botas_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_botas = models.CharField(max_length=20, choices=botas_choices, null=True)
    boton_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_boton = models.CharField(max_length=20, choices=boton_choices, null=True)
    calceti_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_calceti = models.CharField(max_length=20, choices=calceti_choices, null=True)
    calzon_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_calzon = models.CharField(max_length=20, choices=calzon_choices, null=True)
    cierre_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cierre = models.CharField(max_length=20, choices=cierre_choices, null=True)
    collar_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_collar = models.CharField(max_length=20, choices=collar_choices, null=True)
    falda_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_falda = models.CharField(max_length=20, choices=falda_choices, null=True)
    lentes_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_lentes = models.CharField(max_length=20, choices=lentes_choices, null=True)
    panal_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_panal = models.CharField(max_length=20, choices=panal_choices, null=True)
    pantalo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_pantalo = models.CharField(max_length=20, choices=pantalo_choices, null=True)
    pijama_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_pijama = models.CharField(max_length=20, choices=pijama_choices, null=True)
    playera_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_playera = models.CharField(max_length=20, choices=playera_choices, null=True)
    shorts_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_shorts = models.CharField(max_length=20, choices=shorts_choices, null=True)
    sombrer_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_sombrer = models.CharField(max_length=20, choices=sombrer_choices, null=True)
    sueter_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_sueter = models.CharField(max_length=20, choices=sueter_choices, null=True)
    vestido_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_vestido = models.CharField(max_length=20, choices=vestido_choices, null=True)
    zapato_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_zapato = models.CharField(max_length=20, choices=zapato_choices, null=True)
    bigote_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_bigote = models.CharField(max_length=20, choices=bigote_choices, null=True)
    boca_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_boca = models.CharField(max_length=20, choices=boca_choices, null=True)
    brazos_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_brazos = models.CharField(max_length=20, choices=brazos_choices, null=True)
    cabeza_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cabeza = models.CharField(max_length=20, choices=cabeza_choices, null=True)
    cachete_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cachete = models.CharField(max_length=20, choices=cachete_choices, null=True)
    cara_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cara = models.CharField(max_length=20, choices=cara_choices, null=True)
    chichi_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_chichi = models.CharField(max_length=20, choices=chichi_choices, null=True)
    dedos_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_dedos = models.CharField(max_length=20, choices=dedos_choices, null=True)
    dientes_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_dientes = models.CharField(max_length=20, choices=dientes_choices, null=True)
    lengua_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_lengua = models.CharField(max_length=20, choices=lengua_choices, null=True)
    manos1_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_manos1 = models.CharField(max_length=20, choices=manos1_choices, null=True)
    nariz_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_nariz = models.CharField(max_length=20, choices=nariz_choices, null=True)
    ojos_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_ojos = models.CharField(max_length=20, choices=ojos_choices, null=True)
    ombligo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_ombligo = models.CharField(max_length=20, choices=ombligo_choices, null=True)
    orejas_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_orejas = models.CharField(max_length=20, choices=orejas_choices, null=True)
    panza_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_panza = models.CharField(max_length=20, choices=panza_choices, null=True)
    pelo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_pelo = models.CharField(max_length=20, choices=pelo_choices, null=True)
    piernas_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_piernas = models.CharField(max_length=20, choices=piernas_choices, null=True)
    pies_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_pies = models.CharField(max_length=20, choices=pies_choices, null=True)
    rodilla_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_rodilla = models.CharField(max_length=20, choices=rodilla_choices, null=True)
    globo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_globo = models.CharField(max_length=20, choices=globo_choices, null=True)
    juguete_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_juguete = models.CharField(max_length=20, choices=juguete_choices, null=True)
    lapiz_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_lapiz = models.CharField(max_length=20, choices=lapiz_choices, null=True)
    libro_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_libro = models.CharField(max_length=20, choices=libro_choices, null=True)
    muneca_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_muneca = models.CharField(max_length=20, choices=muneca_choices, null=True)
    osito_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_osito = models.CharField(max_length=20, choices=osito_choices, null=True)
    pelota_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_pelota = models.CharField(max_length=20, choices=pelota_choices, null=True)
    tambor_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_tambor = models.CharField(max_length=20, choices=tambor_choices, null=True)
    almohad_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_almohad = models.CharField(max_length=20, choices=almohad_choices, null=True)
    aspirdo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_aspirdo = models.CharField(max_length=20, choices=aspirdo_choices, null=True)
    basura_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_basura = models.CharField(max_length=20, choices=basura_choices, null=True)
    bolsa_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_bolsa = models.CharField(max_length=20, choices=bolsa_choices, null=True)
    botlmam_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_botlmam = models.CharField(max_length=20, choices=botlmam_choices, null=True)
    caja_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_caja = models.CharField(max_length=20, choices=caja_choices, null=True)
    cepidnt_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cepidnt = models.CharField(max_length=20, choices=cepidnt_choices, null=True)
    cepillo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cepillo = models.CharField(max_length=20, choices=cepillo_choices, null=True)
    chupete_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_chupete = models.CharField(max_length=20, choices=chupete_choices, null=True)
    cigarrs_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cigarrs = models.CharField(max_length=20, choices=cigarrs_choices, null=True)
    cobija_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cobija = models.CharField(max_length=20, choices=cobija_choices, null=True)
    cuadro_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cuadro = models.CharField(max_length=20, choices=cuadro_choices, null=True)
    cuchara_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cuchara = models.CharField(max_length=20, choices=cuchara_choices, null=True)
    cuchill_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cuchill = models.CharField(max_length=20, choices=cuchill_choices, null=True)
    dinero_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_dinero = models.CharField(max_length=20, choices=dinero_choices, null=True)
    escoba_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_escoba = models.CharField(max_length=20, choices=escoba_choices, null=True)
    espejo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_espejo = models.CharField(max_length=20, choices=espejo_choices, null=True)
    fotos_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_fotos = models.CharField(max_length=20, choices=fotos_choices, null=True)
    jabon_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_jabon = models.CharField(max_length=20, choices=jabon_choices, null=True)
    llaves_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_llaves = models.CharField(max_length=20, choices=llaves_choices, null=True)
    luz_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_luz = models.CharField(max_length=20, choices=luz_choices, null=True)
    martill_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_martill = models.CharField(max_length=20, choices=martill_choices, null=True)
    medicin_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_medicin = models.CharField(max_length=20, choices=medicin_choices, null=True)
    papel_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_papel = models.CharField(max_length=20, choices=papel_choices, null=True)
    peine_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_peine = models.CharField(max_length=20, choices=peine_choices, null=True)
    plato_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_plato = models.CharField(max_length=20, choices=plato_choices, null=True)
    radio_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_radio = models.CharField(max_length=20, choices=radio_choices, null=True)
    reloj_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_reloj = models.CharField(max_length=20, choices=reloj_choices, null=True)
    taza_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_taza = models.CharField(max_length=20, choices=taza_choices, null=True)
    telefon_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_telefon = models.CharField(max_length=20, choices=telefon_choices, null=True)
    tenedor_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_tenedor = models.CharField(max_length=20, choices=tenedor_choices, null=True)
    tijeras_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_tijeras = models.CharField(max_length=20, choices=tijeras_choices, null=True)
    toalla_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_toalla = models.CharField(max_length=20, choices=toalla_choices, null=True)
    trapo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_trapo = models.CharField(max_length=20, choices=trapo_choices, null=True)
    vaso_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_vaso = models.CharField(max_length=20, choices=vaso_choices, null=True)
    vela_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_vela = models.CharField(max_length=20, choices=vela_choices, null=True)
    bacinic_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_bacinic = models.CharField(max_length=20, choices=bacinic_choices, null=True)
    bano_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_bano = models.CharField(max_length=20, choices=bano_choices, null=True)
    cajon_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cajon = models.CharField(max_length=20, choices=cajon_choices, null=True)
    cama_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cama = models.CharField(max_length=20, choices=cama_choices, null=True)
    cochera_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cochera = models.CharField(max_length=20, choices=cochera_choices, null=True)
    cocina_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cocina = models.CharField(max_length=20, choices=cocina_choices, null=True)
    cuarto_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cuarto = models.CharField(max_length=20, choices=cuarto_choices, null=True)
    cuna_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cuna = models.CharField(max_length=20, choices=cuna_choices, null=True)
    escaler_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_escaler = models.CharField(max_length=20, choices=escaler_choices, null=True)
    estufa_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_estufa = models.CharField(max_length=20, choices=estufa_choices, null=True)
    horno_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_horno = models.CharField(max_length=20, choices=horno_choices, null=True)
    lavabo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_lavabo = models.CharField(max_length=20, choices=lavabo_choices, null=True)
    mesa_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_mesa = models.CharField(max_length=20, choices=mesa_choices, null=True)
    puerta_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_puerta = models.CharField(max_length=20, choices=puerta_choices, null=True)
    recamar_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_recamar = models.CharField(max_length=20, choices=recamar_choices, null=True)
    refrig_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_refrig = models.CharField(max_length=20, choices=refrig_choices, null=True)
    regader_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_regader = models.CharField(max_length=20, choices=regader_choices, null=True)
    ropero_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_ropero = models.CharField(max_length=20, choices=ropero_choices, null=True)
    sala_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_sala = models.CharField(max_length=20, choices=sala_choices, null=True)
    silla_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_silla = models.CharField(max_length=20, choices=silla_choices, null=True)
    sofa_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_sofa = models.CharField(max_length=20, choices=sofa_choices, null=True)
    televis_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_televis = models.CharField(max_length=20, choices=televis_choices, null=True)
    tina_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_tina = models.CharField(max_length=20, choices=tina_choices, null=True)
    ventana_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_ventana = models.CharField(max_length=20, choices=ventana_choices, null=True)
    albrpis_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_albrpis = models.CharField(max_length=20, choices=albrpis_choices, null=True)
    arbol_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_arbol = models.CharField(max_length=20, choices=arbol_choices, null=True)
    calle_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_calle = models.CharField(max_length=20, choices=calle_choices, null=True)
    campo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_campo = models.CharField(max_length=20, choices=campo_choices, null=True)
    casa_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_casa = models.CharField(max_length=20, choices=casa_choices, null=True)
    cielo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cielo = models.CharField(max_length=20, choices=cielo_choices, null=True)
    columpi_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_columpi = models.CharField(max_length=20, choices=columpi_choices, null=True)
    escuela_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_escuela = models.CharField(max_length=20, choices=escuela_choices, null=True)
    estrell_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_estrell = models.CharField(max_length=20, choices=estrell_choices, null=True)
    fiesta_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_fiesta = models.CharField(max_length=20, choices=fiesta_choices, null=True)
    flor_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_flor = models.CharField(max_length=20, choices=flor_choices, null=True)
    iglstmp_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_iglstmp = models.CharField(max_length=20, choices=iglstmp_choices, null=True)
    jardin_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_jardin = models.CharField(max_length=20, choices=jardin_choices, null=True)
    lluvia_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_lluvia = models.CharField(max_length=20, choices=lluvia_choices, null=True)
    luna_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_luna = models.CharField(max_length=20, choices=luna_choices, null=True)
    nieve_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_nieve = models.CharField(max_length=20, choices=nieve_choices, null=True)
    nube_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_nube = models.CharField(max_length=20, choices=nube_choices, null=True)
    parque_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_parque = models.CharField(max_length=20, choices=parque_choices, null=True)
    piedra_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_piedra = models.CharField(max_length=20, choices=piedra_choices, null=True)
    planta_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_planta = models.CharField(max_length=20, choices=planta_choices, null=True)
    playa_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_playa = models.CharField(max_length=20, choices=playa_choices, null=True)
    resbald_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_resbald = models.CharField(max_length=20, choices=resbald_choices, null=True)
    sol_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_sol = models.CharField(max_length=20, choices=sol_choices, null=True)
    techo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_techo = models.CharField(max_length=20, choices=techo_choices, null=True)
    tienmer_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_tienmer = models.CharField(max_length=20, choices=tienmer_choices, null=True)
    zoologi_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_zoologi = models.CharField(max_length=20, choices=zoologi_choices, null=True)
    abuela_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_abuela = models.CharField(max_length=20, choices=abuela_choices, null=True)
    abuelo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_abuelo = models.CharField(max_length=20, choices=abuelo_choices, null=True)
    bebe_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_bebe = models.CharField(max_length=20, choices=bebe_choices, null=True)
    familia_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_familia = models.CharField(max_length=20, choices=familia_choices, null=True)
    hermana_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_hermana = models.CharField(max_length=20, choices=hermana_choices, null=True)
    hermano_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_hermano = models.CharField(max_length=20, choices=hermano_choices, null=True)
    madrina_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_madrina = models.CharField(max_length=20, choices=madrina_choices, null=True)
    maestra_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_maestra = models.CharField(max_length=20, choices=maestra_choices, null=True)
    mama_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_mama = models.CharField(max_length=20, choices=mama_choices, null=True)
    nana_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_nana = models.CharField(max_length=20, choices=nana_choices, null=True)
    nino_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_nino = models.CharField(max_length=20, choices=nino_choices, null=True)
    nina_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_nina = models.CharField(max_length=20, choices=nina_choices, null=True)
    nomnin_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_nomnin = models.CharField(max_length=20, choices=nomnin_choices, null=True)
    padrino_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_padrino = models.CharField(max_length=20, choices=padrino_choices, null=True)
    papa_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_papa = models.CharField(max_length=20, choices=papa_choices, null=True)
    persona_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_persona = models.CharField(max_length=20, choices=persona_choices, null=True)
    senor_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_senor = models.CharField(max_length=20, choices=senor_choices, null=True)
    senora_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_senora = models.CharField(max_length=20, choices=senora_choices, null=True)
    tia_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_tia = models.CharField(max_length=20, choices=tia_choices, null=True)
    tio_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_tio = models.CharField(max_length=20, choices=tio_choices, null=True)
    acerrin_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_acerrin = models.CharField(max_length=20, choices=acerrin_choices, null=True)
    adiosby_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_adiosby = models.CharField(max_length=20, choices=adiosby_choices, null=True)
    besitos_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_besitos = models.CharField(max_length=20, choices=besitos_choices, null=True)
    buendia_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_buendia = models.CharField(max_length=20, choices=buendia_choices, null=True)
    buennoc_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_buennoc = models.CharField(max_length=20, choices=buennoc_choices, null=True)
    cosqlit_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cosqlit = models.CharField(max_length=20, choices=cosqlit_choices, null=True)
    gracias_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_gracias = models.CharField(max_length=20, choices=gracias_choices, null=True)
    hacerme_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_hacerme = models.CharField(max_length=20, choices=hacerme_choices, null=True)
    hola_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_hola = models.CharField(max_length=20, choices=hola_choices, null=True)
    manos2_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_manos2 = models.CharField(max_length=20, choices=manos2_choices, null=True)
    no_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_no = models.CharField(max_length=20, choices=no_choices, null=True)
    ojitos_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_ojitos = models.CharField(max_length=20, choices=ojitos_choices, null=True)
    porfavo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_porfavo = models.CharField(max_length=20, choices=porfavo_choices, null=True)
    salud_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_salud = models.CharField(max_length=20, choices=salud_choices, null=True)
    shhh_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_shhh = models.CharField(max_length=20, choices=shhh_choices, null=True)
    si_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_si = models.CharField(max_length=20, choices=si_choices, null=True)
    tengman_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_tengman = models.CharField(max_length=20, choices=tengman_choices, null=True)
    tortlit_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_tortlit = models.CharField(max_length=20, choices=tortlit_choices, null=True)
    unodstr_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_unodstr = models.CharField(max_length=20, choices=unodstr_choices, null=True)
    abrir_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_abrir = models.CharField(max_length=20, choices=abrir_choices, null=True)
    acabars_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_acabars = models.CharField(max_length=20, choices=acabars_choices, null=True)
    apagar_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_apagar = models.CharField(max_length=20, choices=apagar_choices, null=True)
    apurar_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_apurar = models.CharField(max_length=20, choices=apurar_choices, null=True)
    aventar_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_aventar = models.CharField(max_length=20, choices=aventar_choices, null=True)
    ayudar_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_ayudar = models.CharField(max_length=20, choices=ayudar_choices, null=True)
    bailar_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_bailar = models.CharField(max_length=20, choices=bailar_choices, null=True)
    brincar_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_brincar = models.CharField(max_length=20, choices=brincar_choices, null=True)
    caer_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_caer = models.CharField(max_length=20, choices=caer_choices, null=True)
    caminar_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_caminar = models.CharField(max_length=20, choices=caminar_choices, null=True)
    cantar_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cantar = models.CharField(max_length=20, choices=cantar_choices, null=True)
    cenar_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cenar = models.CharField(max_length=20, choices=cenar_choices, null=True)
    cerrar_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cerrar = models.CharField(max_length=20, choices=cerrar_choices, null=True)
    comer_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_comer = models.CharField(max_length=20, choices=comer_choices, null=True)
    correr_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_correr = models.CharField(max_length=20, choices=correr_choices, null=True)
    dar_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_dar = models.CharField(max_length=20, choices=dar_choices, null=True)
    decir_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_decir = models.CharField(max_length=20, choices=decir_choices, null=True)
    desyuna_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_desyuna = models.CharField(max_length=20, choices=desyuna_choices, null=True)
    dibujar_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_dibujar = models.CharField(max_length=20, choices=dibujar_choices, null=True)
    doler_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_doler = models.CharField(max_length=20, choices=doler_choices, null=True)
    dormir_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_dormir = models.CharField(max_length=20, choices=dormir_choices, null=True)
    empujar_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_empujar = models.CharField(max_length=20, choices=empujar_choices, null=True)
    ensenar_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_ensenar = models.CharField(max_length=20, choices=ensenar_choices, null=True)
    escribi_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_escribi = models.CharField(max_length=20, choices=escribi_choices, null=True)
    esperse_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_esperse = models.CharField(max_length=20, choices=esperse_choices, null=True)
    ir_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_ir = models.CharField(max_length=20, choices=ir_choices, null=True)
    jugar_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_jugar = models.CharField(max_length=20, choices=jugar_choices, null=True)
    lavar_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_lavar = models.CharField(max_length=20, choices=lavar_choices, null=True)
    leer_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_leer = models.CharField(max_length=20, choices=leer_choices, null=True)
    llevar_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_llevar = models.CharField(max_length=20, choices=llevar_choices, null=True)
    llorar_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_llorar = models.CharField(max_length=20, choices=llorar_choices, null=True)
    meterse_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_meterse = models.CharField(max_length=20, choices=meterse_choices, null=True)
    mirar_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_mirar = models.CharField(max_length=20, choices=mirar_choices, null=True)
    mojarse_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_mojarse = models.CharField(max_length=20, choices=mojarse_choices, null=True)
    morder_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_morder = models.CharField(max_length=20, choices=morder_choices, null=True)
    parar_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_parar = models.CharField(max_length=20, choices=parar_choices, null=True)
    pegar_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_pegar = models.CharField(max_length=20, choices=pegar_choices, null=True)
    peinars_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_peinars = models.CharField(max_length=20, choices=peinars_choices, null=True)
    pintar_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_pintar = models.CharField(max_length=20, choices=pintar_choices, null=True)
    poder_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_poder = models.CharField(max_length=20, choices=poder_choices, null=True)
    poner_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_poner = models.CharField(max_length=20, choices=poner_choices, null=True)
    prender_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_prender = models.CharField(max_length=20, choices=prender_choices, null=True)
    querer_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_querer = models.CharField(max_length=20, choices=querer_choices, null=True)
    romper_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_romper = models.CharField(max_length=20, choices=romper_choices, null=True)
    sacar_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_sacar = models.CharField(max_length=20, choices=sacar_choices, null=True)
    secarse_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_secarse = models.CharField(max_length=20, choices=secarse_choices, null=True)
    sentars_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_sentars = models.CharField(max_length=20, choices=sentars_choices, null=True)
    soplar_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_soplar = models.CharField(max_length=20, choices=soplar_choices, null=True)
    subir_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_subir = models.CharField(max_length=20, choices=subir_choices, null=True)
    tener_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_tener = models.CharField(max_length=20, choices=tener_choices, null=True)
    tirar_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_tirar = models.CharField(max_length=20, choices=tirar_choices, null=True)
    tocar_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_tocar = models.CharField(max_length=20, choices=tocar_choices, null=True)
    tomar_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_tomar = models.CharField(max_length=20, choices=tomar_choices, null=True)
    trabaja_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_trabaja = models.CharField(max_length=20, choices=trabaja_choices, null=True)
    ver_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_ver = models.CharField(max_length=20, choices=ver_choices, null=True)
    estar_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_estar = models.CharField(max_length=20, choices=estar_choices, null=True)
    ser_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_ser = models.CharField(max_length=20, choices=ser_choices, null=True)
    ahorita_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_ahorita = models.CharField(max_length=20, choices=ahorita_choices, null=True)
    ayer_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_ayer = models.CharField(max_length=20, choices=ayer_choices, null=True)
    despues_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_despues = models.CharField(max_length=20, choices=despues_choices, null=True)
    dia_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_dia = models.CharField(max_length=20, choices=dia_choices, null=True)
    hoy_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_hoy = models.CharField(max_length=20, choices=hoy_choices, null=True)
    manana_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_manana = models.CharField(max_length=20, choices=manana_choices, null=True)
    noche_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_noche = models.CharField(max_length=20, choices=noche_choices, null=True)
    tempran_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_tempran = models.CharField(max_length=20, choices=tempran_choices, null=True)
    amarill_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_amarill = models.CharField(max_length=20, choices=amarill_choices, null=True)
    azul_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_azul = models.CharField(max_length=20, choices=azul_choices, null=True)
    bonita_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_bonita = models.CharField(max_length=20, choices=bonita_choices, null=True)
    calient_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_calient = models.CharField(max_length=20, choices=calient_choices, null=True)
    cansado_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cansado = models.CharField(max_length=20, choices=cansado_choices, null=True)
    chico_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_chico = models.CharField(max_length=20, choices=chico_choices, null=True)
    content_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_content = models.CharField(max_length=20, choices=content_choices, null=True)
    cuidado_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cuidado = models.CharField(max_length=20, choices=cuidado_choices, null=True)
    difernt_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_difernt = models.CharField(max_length=20, choices=difernt_choices, null=True)
    dificil_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_dificil = models.CharField(max_length=20, choices=dificil_choices, null=True)
    enfermo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_enfermo = models.CharField(max_length=20, choices=enfermo_choices, null=True)
    enojado_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_enojado = models.CharField(max_length=20, choices=enojado_choices, null=True)
    feo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_feo = models.CharField(max_length=20, choices=feo_choices, null=True)
    frio_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_frio = models.CharField(max_length=20, choices=frio_choices, null=True)
    fuchi_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_fuchi = models.CharField(max_length=20, choices=fuchi_choices, null=True)
    grande_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_grande = models.CharField(max_length=20, choices=grande_choices, null=True)
    guapo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_guapo = models.CharField(max_length=20, choices=guapo_choices, null=True)
    hambre_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_hambre = models.CharField(max_length=20, choices=hambre_choices, null=True)
    igual_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_igual = models.CharField(max_length=20, choices=igual_choices, null=True)
    limpio_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_limpio = models.CharField(max_length=20, choices=limpio_choices, null=True)
    lleno_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_lleno = models.CharField(max_length=20, choices=lleno_choices, null=True)
    malo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_malo = models.CharField(max_length=20, choices=malo_choices, null=True)
    miedo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_miedo = models.CharField(max_length=20, choices=miedo_choices, null=True)
    nuevo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_nuevo = models.CharField(max_length=20, choices=nuevo_choices, null=True)
    oscuro_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_oscuro = models.CharField(max_length=20, choices=oscuro_choices, null=True)
    pesado_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_pesado = models.CharField(max_length=20, choices=pesado_choices, null=True)
    poco_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_poco = models.CharField(max_length=20, choices=poco_choices, null=True)
    rojo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_rojo = models.CharField(max_length=20, choices=rojo_choices, null=True)
    roto_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_roto = models.CharField(max_length=20, choices=roto_choices, null=True)
    sed_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_sed = models.CharField(max_length=20, choices=sed_choices, null=True)
    suave_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_suave = models.CharField(max_length=20, choices=suave_choices, null=True)
    sucio_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_sucio = models.CharField(max_length=20, choices=sucio_choices, null=True)
    sueno_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_sueno = models.CharField(max_length=20, choices=sueno_choices, null=True)
    triste_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_triste = models.CharField(max_length=20, choices=triste_choices, null=True)
    vacio_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_vacio = models.CharField(max_length=20, choices=vacio_choices, null=True)
    verde_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_verde = models.CharField(max_length=20, choices=verde_choices, null=True)
    viejo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_viejo = models.CharField(max_length=20, choices=viejo_choices, null=True)
    aquel_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_aquel = models.CharField(max_length=20, choices=aquel_choices, null=True)
    aquela_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_aquela = models.CharField(max_length=20, choices=aquela_choices, null=True)
    el1_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_el1 = models.CharField(max_length=20, choices=el1_choices, null=True)
    ella_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_ella = models.CharField(max_length=20, choices=ella_choices, null=True)
    ellas_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_ellas = models.CharField(max_length=20, choices=ellas_choices, null=True)
    ellos_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_ellos = models.CharField(max_length=20, choices=ellos_choices, null=True)
    esa_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_esa = models.CharField(max_length=20, choices=esa_choices, null=True)
    esas_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_esas = models.CharField(max_length=20, choices=esas_choices, null=True)
    ese_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_ese = models.CharField(max_length=20, choices=ese_choices, null=True)
    eso_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_eso = models.CharField(max_length=20, choices=eso_choices, null=True)
    esos_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_esos = models.CharField(max_length=20, choices=esos_choices, null=True)
    esta_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_esta = models.CharField(max_length=20, choices=esta_choices, null=True)
    estas_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_estas = models.CharField(max_length=20, choices=estas_choices, null=True)
    este_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_este = models.CharField(max_length=20, choices=este_choices, null=True)
    esto_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_esto = models.CharField(max_length=20, choices=esto_choices, null=True)
    estos_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_estos = models.CharField(max_length=20, choices=estos_choices, null=True)
    le_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_le = models.CharField(max_length=20, choices=le_choices, null=True)
    les_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_les = models.CharField(max_length=20, choices=les_choices, null=True)
    lo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_lo = models.CharField(max_length=20, choices=lo_choices, null=True)
    me_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_me = models.CharField(max_length=20, choices=me_choices, null=True)
    mia_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_mia = models.CharField(max_length=20, choices=mia_choices, null=True)
    mias_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_mias = models.CharField(max_length=20, choices=mias_choices, null=True)
    mio_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_mio = models.CharField(max_length=20, choices=mio_choices, null=True)
    mios_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_mios = models.CharField(max_length=20, choices=mios_choices, null=True)
    se_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_se = models.CharField(max_length=20, choices=se_choices, null=True)
    su_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_su = models.CharField(max_length=20, choices=su_choices, null=True)
    te_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_te = models.CharField(max_length=20, choices=te_choices, null=True)
    tu_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_tu = models.CharField(max_length=20, choices=tu_choices, null=True)
    tuya_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_tuya = models.CharField(max_length=20, choices=tuya_choices, null=True)
    tuyas_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_tuyas = models.CharField(max_length=20, choices=tuyas_choices, null=True)
    tuyo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_tuyo = models.CharField(max_length=20, choices=tuyo_choices, null=True)
    tuyos_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_tuyos = models.CharField(max_length=20, choices=tuyos_choices, null=True)
    yo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_yo = models.CharField(max_length=20, choices=yo_choices, null=True)
    como_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_como = models.CharField(max_length=20, choices=como_choices, null=True)
    cual_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_cual = models.CharField(max_length=20, choices=cual_choices, null=True)
    dondest_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_dondest = models.CharField(max_length=20, choices=dondest_choices, null=True)
    porque_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_porque = models.CharField(max_length=20, choices=porque_choices, null=True)
    que_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_que = models.CharField(max_length=20, choices=que_choices, null=True)
    quien_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_quien = models.CharField(max_length=20, choices=quien_choices, null=True)
    el2_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_el2 = models.CharField(max_length=20, choices=el2_choices, null=True)
    la_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_la = models.CharField(max_length=20, choices=la_choices, null=True)
    las_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_las = models.CharField(max_length=20, choices=las_choices, null=True)
    los_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_los = models.CharField(max_length=20, choices=los_choices, null=True)
    un_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_un = models.CharField(max_length=20, choices=un_choices, null=True)
    una_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_una = models.CharField(max_length=20, choices=una_choices, null=True)
    unas_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_unas = models.CharField(max_length=20, choices=unas_choices, null=True)
    unos_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_unos = models.CharField(max_length=20, choices=unos_choices, null=True)
    mas_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_mas = models.CharField(max_length=20, choices=mas_choices, null=True)
    mucho_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_mucho = models.CharField(max_length=20, choices=mucho_choices, null=True)
    nada_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_nada = models.CharField(max_length=20, choices=nada_choices, null=True)
    nohay_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_nohay = models.CharField(max_length=20, choices=nohay_choices, null=True)
    otravez_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_otravez = models.CharField(max_length=20, choices=otravez_choices, null=True)
    tambien_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_tambien = models.CharField(max_length=20, choices=tambien_choices, null=True)
    todo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_todo = models.CharField(max_length=20, choices=todo_choices, null=True)
    ya_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_ya = models.CharField(max_length=20, choices=ya_choices, null=True)
    abajo_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_abajo = models.CharField(max_length=20, choices=abajo_choices, null=True)
    adentro_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_adentro = models.CharField(max_length=20, choices=adentro_choices, null=True)
    afuera_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_afuera = models.CharField(max_length=20, choices=afuera_choices, null=True)
    ahi_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_ahi = models.CharField(max_length=20, choices=ahi_choices, null=True)
    allaall_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_allaall = models.CharField(max_length=20, choices=allaall_choices, null=True)
    aqui_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_aqui = models.CharField(max_length=20, choices=aqui_choices, null=True)
    arriba_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_arriba = models.CharField(max_length=20, choices=arriba_choices, null=True)
    atras_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_atras = models.CharField(max_length=20, choices=atras_choices, null=True)
    encima_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_encima = models.CharField(max_length=20, choices=encima_choices, null=True)
    de_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_de = models.CharField(max_length=20, choices=de_choices, null=True)
    en_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_en = models.CharField(max_length=20, choices=en_choices, null=True)
    para_choices = [(u'understands', u'understands'), (u'produces', u'produces')]
    item_para = models.CharField(max_length=20, choices=para_choices, null=True)
