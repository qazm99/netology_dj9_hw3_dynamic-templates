from django import template
from datetime import datetime, time


register = template.Library()


@register.filter
def format_date(date_in):
    if isinstance(date_in, float) or isinstance(date_in, int):
        delta_ = (datetime.now() - datetime.fromtimestamp(date_in))
        if delta_.total_seconds() < 60*10+6000:
            return "Только что"
        elif delta_.total_seconds() < 60*60*24:
            num_hours = int(delta_.total_seconds()//3600)
            if (str(num_hours)[-1:] == '1') and (str(num_hours)[-2:-1] != '1'):
                name_hours = 'час'
            elif (str(num_hours)[-1:] in '234') and (str(num_hours)[-2:-1] != '1'):
                name_hours = 'часа'
            else:
                name_hours = 'часов'
            return f'{num_hours} {name_hours} назад'
        else:
            return datetime.fromtimestamp(date_in).strftime('%Y-%m-%d')
    else:
        return date_in

# необходимо добавить фильтр для поля `score`
@register.filter
def format_score(in_score):
    out_score = 'Скоро узнаем'
    if isinstance(in_score, int):
        if in_score < -5:
            out_score = 'Всё плохо'
        elif in_score <= 5:
            out_score = 'Нейтрально'
        elif in_score > 5:
            out_score = 'Хорошо'
    return out_score

@register.filter
def format_num_comments(comments_count):
    if isinstance(comments_count, int):
        if comments_count > 50:
            return '50+'
        elif comments_count > 0:
            return comments_count
    return 'Оставьте комментарий'

@register.filter
def format_selftext(text, words_count):
    if isinstance(text, str) and isinstance(words_count, int):
        split_list = text.split()
        format_text = ''
        if len(split_list) > words_count*2:
            format_text = ' '.join(split_list[:words_count])+' ... '+' '.join(split_list[-words_count:])
        elif len(split_list) > 0:
            format_text = text
        return format_text





