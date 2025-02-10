def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    pos_mm, pos_ss = map(int, pos.split(":"))
    m_pos = pos_mm * 60+pos_ss
    
    op_start_mm, op_start_ss = map(int, op_start.split(":"))
    m_op_start = op_start_mm*60 + op_start_ss
    
    op_end_mm, op_end_ss = map(int, op_end.split(":"))
    m_op_end = op_end_mm*60+op_end_ss
    
    video_len_mm, video_len_ss = map(int, video_len.split(":"))
    m_video_len = video_len_mm*60+video_len_ss
    
    if m_op_start <= m_pos <= m_op_end:
        m_pos = m_op_end

    for command in commands:
        if command == "next":
            m_pos = min(m_pos + 10, m_video_len) 
        elif command == "prev":
            m_pos = max(m_pos - 10, 0)         
            
        if m_pos >= m_op_start and m_pos <= m_op_end:
            m_pos = m_op_end
    
    answer = f"{m_pos//60:02}:{m_pos%60:02}"
    return answer