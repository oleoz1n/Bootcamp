def dia_semana(diaSemana):
    match(diaSemana).lower():
        case 'sunday':
            return 1 
        case 'monday':
            return 2
        case 'tuesday':
            return 3
        case 'wednesday':
            return 4
        case 'thursday':
            return 5
        case 'friday':
            return 6
        case 'saturday':
            return 7
        case _:
            return ''
def nome_dia(diaSemana):
    if diaSemana != '':
        diaSemana = f'{(diaSemana/7):.2f}'
        diaSemana = int(diaSemana[-2:len(diaSemana)])
        match(diaSemana):
            case 14:
                diaSemana = ', Sunday'
            case 29:
                diaSemana = ', Monday'
            case 43:
                diaSemana = ', Tuesday'
            case 57:
                diaSemana = ', Wednesday'
            case 71:
                diaSemana = ', Thursday'
            case 86:
                diaSemana = ', Friday'
            case 0:
                diaSemana = ', Saturday'
    return diaSemana

def time_calculator(time1, maistime,diaSemana=''):
    if time1[2] == ':':
        hora = int(time1[(len(time1)-len(time1)):(len(time1)-(len(time1)+6))])
        min = int(time1[(len(time1)-(len(time1)-3)):(len(time1)-(len(time1)+3))])
    elif time1[1] == ':':
        hora = int(time1[(len(time1)-len(time1)):(len(time1)-(len(time1)+6))])
        min = int(time1[(len(time1)-(len(time1)-2)):(len(time1)-(len(time1)+3))])
    amOrPm = time1[len(time1)-2:len(time1)]

    if maistime[1] == ':':
        maisHora = int(maistime[(len(maistime)-len(maistime)):(len(maistime)-(len(maistime)+3))])
        maisMin = int(maistime[(len(maistime)-(len(maistime)-2)):(len(maistime)-(len(maistime)-4))])
    elif maistime[2] == ':':
        maisHora = int(maistime[(len(maistime)-len(maistime)):(len(maistime)-(len(maistime)+3))])
        maisMin = int(maistime[(len(maistime)-(len(maistime)-3)):(len(maistime)-(len(maistime)-5))])
    elif maistime[3] == ':':
        maisHora = int(maistime[(len(maistime)-len(maistime)):(len(maistime)-(len(maistime)+3))])
        maisMin = int(maistime[(len(maistime)-(len(maistime)-4)):(len(maistime)-(len(maistime)-6))])

    
    hora += maisHora
    min += maisMin
    if min > 60:
        hora += int(min/60)
        min = min - (int(min/60)*60)
    elif min == 60:
        min = '00'
    if min < 10:
        min = f'0{min}'

    diaSemana = dia_semana(diaSemana)

    if amOrPm == "AM":
        pass
    elif amOrPm == "PM":
        hora += 12
    
    if hora > 24:
            dia = int(hora/24)
            if diaSemana != '':
                diaSemana = nome_dia(diaSemana+dia)
                    
            hora -= dia*24
            
            if dia == 1:
                if 24 > hora > 12:
                    result = f'{(hora-12)}:{min} PM{diaSemana} (next day)'
                elif hora == 12:
                    result = f'{(hora)}:{min} AM{diaSemana} (next day)'
                elif hora == 24:
                    result = f'{(hora-12)}:{min} PM{diaSemana} (next day)'
                elif hora == 0:
                    result = f'{(hora+12)}:{min} AM{diaSemana} (next day)'
                else:
                    result = f'{hora}:{min} AM{diaSemana} (next day)'
            
            if dia > 1:
                if 24 > hora > 12:
                    result = f'{(hora-12)}:{min} PM{diaSemana} ({dia} days later)'
                elif hora == 12:
                    result = f'{(hora)}:{min} AM{diaSemana} ({dia} days later)'
                elif hora == 24:
                    result = f'{(hora-12)}:{min} PM{diaSemana} ({dia} days later)'
                elif hora == 0:
                    result = f'{(hora+12)}:{min} AM{diaSemana} ({dia} days later)'
                else:
                    result = f'{hora}:{min} AM{diaSemana} ({dia} days later)'
    else:
        diaSemana = nome_dia(diaSemana)
        if 24 > hora > 12:
            result = f'{(hora-12)}:{min} PM{diaSemana}'
        elif hora == 12:
            result = f'{(hora)}:{min} PM{diaSemana}'
        elif hora == 24:
            result = f'{(hora-24)}:{min} AM{diaSemana}'
        elif hora == 0:
            result = f'{(hora+12)}:{min} AM{diaSemana}'
        else:
            result = f'{hora}:{min} AM{diaSemana}'


    return result
