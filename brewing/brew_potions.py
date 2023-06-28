import brewing.potion_class as potion_class
import brewing.containers as containers
import brewing.cooking as cooking
import brewing.inspection as inspection
# import brewing.ingredients as ingredients


def make_example_potion(student_name):
    my_potion = potion_class.Potion(student_name=student_name)
    # Set up your old kettle and light an eternal flame underneath it.
    my_potion.setup(container=containers.old_kettle, heat_source=cooking.eternal_flame)
    # Simmer for 5 hours.
    cooking.simmer(my_potion, duration=5)
    print("You have successfully run make_example_potion, well done :).")
    return my_potion


def make_python_expert_potion(student_name):
    print("I am a Python Expert")
    # todo: write this function!
    my_potion = potion_class.Potion(student_name=student_name)
    my_potion.setup(
        container=containers.pewter_cauldron, 
        heat_source=cooking.fire)
    my_potion.add_ingredients(ingredients=['fish_eyes', 'tea_leaves', 'unicorn_hair'])
    cooking.simmer(my_potion, duration=2)
    return my_potion


if __name__ == "__main__":
    student_name = 'Karina-Daniel'
    #my_potion = make_example_potion(student_name=my_name)
    # Let Snape inspect the potion
    #inspection.inspection_by_Snape(potion=my_potion, target_potion='example_potion')
    my_potion = make_python_expert_potion(student_name)
    inspection.inspection_by_Snape(potion=my_potion, target_potion='python_expert')