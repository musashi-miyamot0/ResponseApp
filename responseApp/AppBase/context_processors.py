
def menu_data(request) -> dict[str,list[dict[str,str]]]:
    menu = [{'title':'Все отзывы','urlLink':'allresponse'},]
    data = {
        'mainmenu':menu,
    }
    return data 