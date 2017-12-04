from owlready2 import *
path = "file://D:/INZ/Guns.owl"
onto = get_ontology(path).load()

###########################
value_from_onclick = 'Anaconda'
###########################

def one_word_analysis():

    # potrzebne do wyboru ktorej funkcji uzyc dla slowa (zaleznie czy jest klasa czy indywiduum + zmienne globalne:
    classes = list(onto.classes()) #GLOBAL LIST
    def cut_the_class():
        cut_classes = list()
        for every_class in classes:
            cut_classes.append(str(every_class).split('.')[1])
        return cut_classes
    cut_classes_list = cut_the_class()   # wycieta lista wszystkich klas ze slownika

    individuals = list(onto.individuals())#GLOBAL LIST
    def cut_the_individual():
        cut_individuals = list()
        for every_individual in individuals:
            cut_individuals.append(str(every_individual).split('.')[1])
        return cut_individuals
    cut_individual_list = cut_the_individual()  # wycieta lista wszystkich indywiduów ze slownika
######!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


    cut_the_object_property_list= list(onto.object_properties())
    def cut_the_object_property():
        cut_object_property = list()
        for every_class in cut_the_object_property_list:
            cut_object_property.append(str(every_class).split('.')[1])
        return cut_object_property
#######!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    def classes_with_power():  # funkcja do przypisywania klasom "sily". Potrzebne tylko do funkcji sortujacej.
        power_of_classes = dict()
        list_of_classes_with_powers = list()
        for one_class in classes:
            cutted_class = str(one_class).split('.')[-1]
            temporary_code = ("onto.search(subclass_of= onto." + cutted_class + ")")
            power_of_classes.update({cutted_class: list(eval(temporary_code))})
        for key, value in sorted(power_of_classes.items()):
            list_of_classes_with_powers.append(str(len([item for item in value if item])) + '.' + key)
        return list_of_classes_with_powers


    def classes_above_individuals():  # zwraca klasy w ktorych znajduje sie inwdywiduum (funkcja tylko dla indywiduum)
        individuals_result = dict()
        classes_above_individuals_result = dict()
        for one in individuals:
            cutted_individuals = str(one).split('.')[1]
            individuals_result[cutted_individuals] = []
            for two in classes:
                cutted_classes = str(two).split('.')[1]
                individuals_of = "onto.search(type= onto." + cutted_classes + ")"
                if one in eval(individuals_of):
                    individuals_result[cutted_individuals].append(cutted_classes)
        for one in individuals_result:
            classes_above_individuals_result.update({one: individuals_result[one]})
        return classes_above_individuals_result



    def classes_above_class():
        classes_above_class_result = dict()
        for one in classes:
            cutted_classes = str(one).split('.')[1]
            classes_above_class_result[cutted_classes] = []
            for two in classes:
                cutted_classes_2 = str(two).split('.')[1]
                classes_of = "onto.search(subclass_of= onto." + cutted_classes_2 + ")"
                if one in eval(classes_of):
                    classes_above_class_result[cutted_classes].append(cutted_classes_2)
        for one in classes_above_class_result:
            classes_above_class_result.update({one: classes_above_class_result[one]})
        return classes_above_class_result


    def sorted_above():   # sortuje klasy powyzej slowa (to jest funkcja dla indywiduum i dla klasy)
        def comparision():
            dict_for_going_up = dict()
            dict_for_going_up.update(classes_above_individuals())
            dict_for_going_up.update(classes_above_class())
            one_object_classes = (dict_for_going_up[value_from_onclick])
            list_to_compare = classes_with_power()
            index = -1
            for one in one_object_classes:
                index = index+1
                for two in list_to_compare:
                    if one == str(two).split('.')[-1]:
                        one_object_classes[index] = two
            else:
                pass
            return sorted(one_object_classes, reverse=True)

        def updated_hierarchy_of_classes():
            temp = comparision()
            i = 0
            for every in temp:
                temp[i] = (str(every).split('.')[-1])
                i = i + 1
            return temp
        result_sorted_above = updated_hierarchy_of_classes()
        return result_sorted_above


    def class_directly_above():  # oddaje bezposrednią nadklase dla slowa
        class_above = sorted_above()
        return class_above[-1]


    def instances_from_the_same_class():  # jesli slowo = instancja -> wyswietl wszystkie instancje z tej samej klasy
        class_above = class_directly_above()
        temp = "onto.search(type= onto." + class_above + ")"
        temp_evaluated = eval(temp)
        print(temp_evaluated)
        result = []
        for every_class in temp_evaluated:
            if (str(every_class).split('.')[1]) == value_from_onclick:
                pass
            else:
                result.append(str(every_class).split('.')[1])

        return result


    def instances_from_the_clicked_class():  # jesli slowo = klasa -> wyswietl wszystkie instancje tej klasy
        the_class = value_from_onclick
        temp = "onto.search(type= onto." + the_class + ")"
        temp_evaluated = eval(temp)
        result = []
        for every_class in temp_evaluated:
            if (str(every_class).split('.')[1]) == value_from_onclick:
                pass
            else:
                result.append(str(every_class).split('.')[1])
        return result

    def classes_below():
        eval_code = "onto.search(subclass_of= onto." + value_from_onclick + ")"
        result = eval(eval_code)
        result2 = list()
        for every_class in result:
            result2.append(str(every_class).split('.')[1])
        return result2
    ######################
    ######################
    ######################

    properties = cut_the_object_property()
    with onto:
        class temporary(Thing):
            pass

    def relations():
        temp = temporary(str(value_from_onclick))
        temporary_list = list()
        for every_property in properties:
            temp2 = getattr(temp, every_property)
            if (temp2) == None:
                pass
            elif len(temp2) == 0:
                pass
            else:
                for i in range(len(temp2)):
                    temp3 = list(temp2)
                    a = value_from_onclick
                    b = every_property
                    c = temp3[i]
                    temporary_list.append((str(a) + ' ' + (str(b) + ' ' + str(c).split('.')[-1])))
        relations_result = list(set(temporary_list))
        return relations_result


    ##################################################
    ###################################################
    ###################################################

    LIST=[]

    #DATA FOR WORD IF WORD IS A INDIVIDUAL
    for every in cut_individual_list:
        if every == value_from_onclick:
            print ('INDIVIDUAL')
            INDI_val1=sorted_above()
            LIST.append(INDI_val1)
            INDI_val2=instances_from_the_same_class()
            LIST.append(INDI_val2)
            INDI_val3=relations()
            LIST.append(INDI_val3)
        else:
            pass

    for every in cut_classes_list:
            if every == value_from_onclick:
                print('CLASS')
                CLASS_val1=sorted_above()
                LIST.append(CLASS_val1)
                CLASS_val2=classes_below()
                LIST.append(CLASS_val2)
                CLASS_val3=instances_from_the_clicked_class()
                LIST.append(CLASS_val3)
            else:
                pass
    #DATA FOR WORD IF WORD IS A CLASS

    return LIST

zmienna=one_word_analysis()
print(zmienna[2])