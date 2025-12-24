def color_text(text, color_ryb, font_size=12, bold=True, text_color=False):
    if not text_color:
        text_color = '#ffffff' if sum(color_ryb._ryb)/3 > 180 else '#000000'
    else:
        text_color = text_color.hex
    hex_color = color_ryb.hex
    return f"""
        <span style="
            font-size: {font_size}px;
            background-color: {hex_color};
            color: {text_color};
            padding: 0.1em 0.1em;
            border-radius: 0.3em;
            {'font-weight: bold;' if bold else ''}">
            {text}
        </span>
        """

def color_title(text, color_ryb, font_size=32, bold=True, text_color=False):
    if not text_color:
        text_color = '#ffffff' if sum(color_ryb._ryb)/3 > 180 else '#000000'
    else:
        text_color = text_color.hex
    hex_color = color_ryb.hex
    return f"""
        <span style="
            font-size: {font_size}px;
            background-color: {hex_color};
            color: {text_color};
            padding: 0.2em 0.5em;
            border-radius: 0.3em;
            {'font-weight: bold;' if bold else ''}">
            {text}
        </span>
        """

def calculate_score(answers, q_list):
    '''return `r_score, y_score, b_score` out of `r, y, b`'''
    r = 0
    y = 0
    b = 0
    for q in range(12):
        i = [i for i, a in enumerate(q_list[q].answers) if a.text == answers[q]][0]
        r += q_list[q].answers[i].r
        y += q_list[q].answers[i].y
        b += q_list[q].answers[i].b
    # ----- 1-10 scoring -----
    # r_score = round((r / 15) * 9 + 1)
    # y_score = round((y / 14) * 9 + 1)
    # b_score = round((b / 14) * 9 + 1)
    # ----- 0-10 scoring -----
    r_score = round((r / 15) * 10)
    y_score = round((y / 14) * 10)
    b_score = round((b / 14) * 10)
    return r_score, y_score, b_score
