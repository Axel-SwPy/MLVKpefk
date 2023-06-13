def show_all_var(choise_slug_img):
    random_list = []
    linked_list_value = []
    
    show_variant = [('Варіант 1', 1), ('Варіант 52', 1), ('Варіант 3', 1), ('Варіант 4', 1), ('Варіант 1', 2), ('Варіант 2', 2), ('Варіант 3', 2)]
    slug_from_photo = [('practice-1-variant-1',), ('practice-1-variant-2',), ('practice-1-variant-3',), ('practice-2-variant-1',)]

    split_slug = choise_slug_img.rsplit("-")
    sort_pract_index = split_slug[1]

    for item_slug in slug_from_photo:
        item_slug_split = item_slug[0].rsplit("-")
        pract_id = item_slug_split[1]
        variant_id = item_slug_split[3]
        if str(pract_id) == str(sort_pract_index):
            random_list.append(item_slug[0])
            for item_variant in show_variant:
                if str(item_variant[0][-1]) == str(variant_id) and str(item_variant[1]) == str(pract_id):
                    linked_list_value.append([item_variant[0], item_slug[0]])
                
                    

    print(linked_list_value)

show_all_var('practice-1-variant-1')
