#TODO 僅做好介面部分

import gradio as gr

font = font =[ 
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

def enigma_simulation(rotor1, rotor2, rotor3, plugboard ,text):
    """
    模擬恩尼格碼機的加密過程
    
    參數:
    rotor1, rotor2, rotor3 (int): 三個轉子的位置 (1-26)
    plugboard (str): 接線板設置

    返回:
    str: 
    
    A~Z 65~90
    """
    

# 創建 Gradio 界面
interface = gr.Interface(
    fn=enigma_simulation,
    inputs=[
        gr.Slider(0, 26, step=1, label="左轉子"),
        gr.Slider(0, 26, step=1, label="中轉子"),
        gr.Slider(0, 26, step=1, label="右轉子"),
        gr.Textbox(label="接線板設置 (例如: AB CD EF)"),
        gr.Textbox(label="輸入字母", max_lines=1, placeholder="輸入單個字母", value="A"),
        gr.Radio(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],label="鍵盤"),
    ],
    outputs=gr.Textbox(label="模擬結果"),
    title="恩尼格碼機模擬器",
    description="調整轉子位置和設置接線板來模擬恩尼格碼機的設置。"
)

# 啟動界面
interface.launch()