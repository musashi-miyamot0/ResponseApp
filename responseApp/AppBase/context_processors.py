
def menu_data(request) -> dict[str,list[dict[str,str]]]:
    prefix_path_svg='svg'
    menu = [{'title':'Главная','urlLink':'home','ico':f'{prefix_path_svg}/home.svg'},
            {"title":'Профиль','urlLink':'register:view_profile','ico':f'{prefix_path_svg}/profile.svg'},
            {"title":'Настройки','urlLink':'','ico':f'{prefix_path_svg}/settings.svg'},
            
            ]
    data = {
        'mainmenu':menu,
    }
    return data 