# -*- coding: utf-8 -*-
import tkinter as tk
from PIL import ImageTk, Image
import tkinter.font as tkFont
import os
import cv2
import time

# 放你們自己的檔案路徑
os.chdir("D:\\github\\PBC_final_project")


class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('搶銀行')
        self.pics_in_bag = []
        self.canvas = tk.Canvas(width=1248, height=702)
        self.canvas.pack()
        self.issecond = False

        # 放背景圖
        self.back = Image.open('金庫背景.jpg')
        self.back = self.back.resize((1248, 702))
        self.back = ImageTk.PhotoImage(self.back)
        self.get_back = self.canvas.create_image(0,0, image=self.back, anchor='nw')

        # 放灑水器
        self.wa = Image.open("灑水器.png")
        self.wa = self.wa.resize((35,35))
        self.wa = ImageTk.PhotoImage(self.wa)
        wa = self.canvas.create_image(525,30, image=self.wa, anchor='n')
        
	    # 放警報器
        self.si = Image.open("警報器.png")
        self.si = self.si.resize((50,50))
        self.si = ImageTk.PhotoImage(self.si)
        si = self.canvas.create_image(725,25, image=self.si, anchor='n')
		# 點擊警報器觸發機關
        self.canvas.tag_bind(si,"<Button-1>", lambda e:[click_si(self)])
		# 警報器機關
        def click_si(self):
            self.red = Image.open('redred.png')
            self.red = self.red.resize((1248, 702))
            self.red = ImageTk.PhotoImage(self.red)
            red = self.canvas.create_image(0,0, image=self.red, anchor='nw')
			# 放對話框
            self.dlg = Image.open("對話框.png")
            self.dlg = self.dlg.resize((1000,550))
            self.dlg = ImageTk.PhotoImage(self.dlg)
            dlg = self.canvas.create_image(624,310, image=self.dlg, anchor='n')

            #放對話框
            text = self.canvas.create_text(628,580,
                   text = "亂點警報器會被警衛發現！ 螢幕變紅色！",
                   font = (False, 20), 
                   fill = "white",
                   anchor = "n")
            #放返回鍵
            self.re_button = Image.open("回主畫面.png")
            self.re_button = self.re_button.resize((50,50))
            self.re_button = ImageTk.PhotoImage(self.re_button)
            re_button = self.canvas.create_image(1000, 630, image = self.re_button)
            self.canvas.tag_bind(re_button,"<Button-1>",
		        lambda e:[self.canvas.delete(re_button),self.canvas.delete(dlg),self.canvas.delete(text), self.canvas.delete(red)])

        # 放椅子
        self.op = Image.open("椅子.png")
        self.op = self.op.resize((300, 300))
        self.op = ImageTk.PhotoImage(self.op) 
        op = self.canvas.create_image(250,400, image=self.op)
        # 放桌子
        self.tb = Image.open("桌子.png")
        self.tb = self.tb.resize((300, 300))
        self.tb = ImageTk.PhotoImage(self.tb) 
        tb = self.canvas.create_image(320,450, image=self.tb)

        # 放監視器
        self.sp = Image.open("監視器.png")
        self.sp = self.sp.resize((75,75))
        self.sp = ImageTk.PhotoImage(self.sp)
        sp = self.canvas.create_image(950,50, image=self.sp, anchor='n')
		# 點擊監視器觸發機關
        self.canvas.tag_bind(sp,"<Button-1>", lambda e:[click_sp(self), self.countdown(sprec = 0)])
        
        # 監視器機關
        def click_sp(self):
            self.show_info("你亂點監視器會被警衛發現！ 剩餘時間減少1分鐘")
        
        # 放地毯
        self.bk = Image.open("地毯.png")
        self.bk = self.bk.resize((600,50))
        self.bk = ImageTk.PhotoImage(self.bk)
        bk = self.canvas.create_image(650,500, image=self.bk, anchor='n')          

        # 放對話框
        self.dlg = Image.open("對話框.png")
        self.dlg = self.dlg.resize((1000,550))
        self.dlg = ImageTk.PhotoImage(self.dlg)
        dlg = self.canvas.create_image(624,310, image=self.dlg, anchor='n')
        
        # 放音符
        self.noteSymbol = Image.open("音符.png")
        self.noteSymbol = self.noteSymbol.resize((65, 65))
        self.noteSymbol = ImageTk.PhotoImage(self.noteSymbol) 
        noteSymbol = self.canvas.create_image(300,450, image=self.noteSymbol)
        # self.canvas.pack()
        self.noteSymbol_big = Image.open("音符_白底.png")
        self.noteSymbol_big = self.noteSymbol_big.resize((450, 400))

        
        # 放對話框
        self.show_info("現在，你要設法打開金庫的門闖進金庫，\n若倒數時間到，則保安趕到，搶劫計畫即會失敗!")
        
        # 放金庫門
        self.door = Image.open('金庫門.png')
        self.door = self.door.resize((300, 260))
        self.door = ImageTk.PhotoImage(self.door)
        self.door = self.canvas.create_image(470,180, image=self.door, anchor='nw')
        # self.canvas.tag_bind(door, "<Button-1>",  self.second())
        # 我把這句換地方放
        # self.canvas.tag_bind(door, "<Button-1>", lambda e:[video_play(), self.second()])
        
        # 放時鐘
        self.clock = Image.open("時鐘.png")
        self.clock = self.clock.resize((65, 65))
        self.clock = ImageTk.PhotoImage(self.clock)
        clock = self.canvas.create_image(400,120, image=self.clock)
        self.canvas.pack()

        # 點擊時鐘觸發機關
        self.canvas.tag_bind(clock,"<Button-1>", lambda e:[click_clock(self)])
        
        # 時鐘機關
        def click_clock(self):
            # self.frameC = locked_clock(self)  # 機關我寫在clock organ 的資料夾內
            self.locked_clock = self.canvas.create_window(450,50, anchor="nw", window = locked_clock(self), width = 380, height = 700)
        
        # 音符機關
        def click_note(self):
            self.noteSymbol_big = Image.open("音符_白底.png")
            self.noteSymbol_big = self.noteSymbol_big.resize((450, 400))
            self.noteSymbol_big = ImageTk.PhotoImage(self.noteSymbol_big)
            noteSymbol_big = self.canvas.create_image(624,350, image=self.noteSymbol_big)
            #放返回鍵
            self.close_button = Image.open("close.png")
            self.close_button = self.close_button.resize((25,25))
            self.close_button = ImageTk.PhotoImage(self.close_button)
            close_button = self.canvas.create_image(800, 200, image = self.close_button)
            self.canvas.tag_bind(close_button,"<Button-1>",lambda e:[self.canvas.delete(noteSymbol_big),self.canvas.delete(close_button)])
        
        # 音符機關設置
        self.canvas.tag_bind(noteSymbol,"<Button-1>", lambda e:[click_note(self)])

        # 放盆栽
        self.plant = Image.open("盆栽.png")
        self.plant = self.plant.resize((100, 100))
        self.plant = ImageTk.PhotoImage(self.plant)
        plant = self.canvas.create_image(1000,400, image=self.plant, anchor='n')

        # 盆栽機關設置
        self.canvas.tag_bind(plant, "<Button-1>", lambda e:[self.canvas.move(plant, 0, -100),self.canvas.itemconfigure(handsome, state = "normal")])
        
        # 放上令傑ㄉ帥照
        self.handsome = Image.open("令傑ㄉ帥照.jpg")
        self.handsome = self.handsome.resize((90,90))
        self.handsome = ImageTk.PhotoImage(self.handsome)
        self.handsome1 = Image.open("令傑ㄉ帥照.jpg")
        self.handsome1 = self.handsome1.resize((80,80))
        self.handsome1 = ImageTk.PhotoImage(self.handsome1)
        handsome = self.canvas.create_image(1000,400,image = self.handsome)
        self.canvas.itemconfigure(handsome, state = "hidden")
         #讓令傑飛一會兒
        self.canvas.tag_bind(handsome, "<Button-1>", lambda a:[self.canvas.move(handsome, -950, -200), self.canvas.delete(handsome),
                             self.canvas.create_image(130, 145, image=self.handsome1, anchor='n')])
        
        # 倒數計時器
        self.label = tk.Label(self, text="", width=7, font=("Arial", 20), bg = "lightsteelblue")
        self.label.pack()
        self.remaining = 0
        self.countdown(600, sprec = 100)  # 設定時間

        # 道具欄
        self.image = Image.open("道具欄.png").resize((150,300))
        self.column_img = ImageTk.PhotoImage(self.image)
        self.can_pic_column = self.canvas.create_image(90, 150, image=self.column_img, anchor='n')

        # 撿道具（道具消失、出現在道具欄）
        # self.canvas.tag_bind(self.can_pic_tool,"<Button-1>",lambda e:[self.canvas.delete(self.can_pic_tool),
        #                      self.canvas.create_image(300, 300, image=self.Tool_img, anchor='n')])
    # 過場動畫
    def video_play(self):  
        cap = cv2.VideoCapture('Cutscenes.mp4')
        while(cap.isOpened()):
            ret, frame = cap.read()
            time.sleep(0.02)  # 播放倍速
            if ret == False:
                break
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()


    # 進入第二關
    def second(self):
        self.total_value = 0
        self.back2 = Image.open('back2.png')
        self.back2 = self.back2.resize((1248, 702))
        self.back2 = ImageTk.PhotoImage(self.back2)
        self.canvas.create_image(0,0, image=self.back2, anchor='nw')
        self.issecond = True

        # 道具欄（浮上來）
        self.canvas.tag_raise(self.can_pic_column)
       

        # 所有寶石圖片放置
        # 古董區
        self.exp_paint = Image.open("jwellery/96.7e.jpg").resize((50,80))
        self.expensive_paint = ImageTk.PhotoImage(self.exp_paint)
        can_expensive_paint = self.canvas.create_image(525, 200, image=self.expensive_paint, anchor='n')
        self.exp_paint1 = Image.open("jwellery/96.7e.jpg").resize((25,40))
        self.expensive_paint1 = ImageTk.PhotoImage(self.exp_paint1)
        self.canvas.tag_bind(can_expensive_paint, "<Button-1>", lambda e:[self.put_item(can_expensive_paint, 1)])
    

        self.exp_statue = Image.open("jwellery/18.4e.png").resize((50,100))
        self.expensive_statue = ImageTk.PhotoImage(self.exp_statue)
        can_expensive_statue = self.canvas.create_image(230, 480, image=self.expensive_statue, anchor='n')
        self.exp_statue1 = Image.open("jwellery/18.4e.png").resize((25,50))
        self.expensive_statue1 = ImageTk.PhotoImage(self.exp_statue1)
        self.canvas.tag_bind(can_expensive_statue, "<Button-1>", lambda e:[self.put_item(can_expensive_statue, 2)])

        self.exp_hum_statue = Image.open("jwellery/45.5e.png").resize((200,300))
        self.expensive_human_statue = ImageTk.PhotoImage(self.exp_hum_statue)
        can_expensive_human_statue = self.canvas.create_image(750, 240, image=self.expensive_human_statue, anchor='n')
        self.exp_hum_statue1 = Image.open("jwellery/45.5e.png").resize((50,75))
        self.expensive_human_statue1 = ImageTk.PhotoImage(self.exp_hum_statue1)
        self.canvas.tag_bind(can_expensive_human_statue, "<Button-1>", lambda e:[self.put_item(can_expensive_human_statue, 3)])

        self.exp_veg = Image.open("jwellery/翠玉白菜.png").resize((70,100))
        self.expensive_vegetable = ImageTk.PhotoImage(self.exp_veg)
        can_expensive_vegetable = self.canvas.create_image(1220, 590, image=self.expensive_vegetable, anchor='n')
        self.exp_veg1 = Image.open("jwellery/翠玉白菜.png").resize((35,50))
        self.expensive_vegetable1 = ImageTk.PhotoImage(self.exp_veg1)
        self.canvas.tag_bind(can_expensive_vegetable, "<Button-1>", lambda e:[self.put_item(can_expensive_vegetable, 4)])

        self.exp_vast = Image.open("jwellery/清代花瓶.png").resize((60,90))
        self.expensive_vast = ImageTk.PhotoImage(self.exp_vast)
        can_expensive_vast = self.canvas.create_image(385, 450, image=self.expensive_vast, anchor='n')
        self.exp_vast1 = Image.open("jwellery/清代花瓶.png").resize((30,45))
        self.expensive_vast1 = ImageTk.PhotoImage(self.exp_vast1)
        self.canvas.tag_bind(can_expensive_vast, "<Button-1>", lambda e:[self.put_item(can_expensive_vast, 5)])

        
         # 寶石區
        self.jew_gold_2 = Image.open("jwellery/金條.png").resize((50,50))
        self.gold_2 = ImageTk.PhotoImage(self.jew_gold_2)
        self.jew_gold = Image.open("jwellery/金條.png").resize((60,70))
        self.gold = ImageTk.PhotoImage(self.jew_gold)
        can_gold = self.canvas.create_image(50, 580, image=self.gold, anchor='n')
        self.canvas.tag_bind(can_gold, "<Button-1>", lambda e:[self.put_item(can_gold, 6)])

        self.jwe_pink_2 = Image.open("jwellery/1.1e粉紅鑽.png").resize((50,50))
        self.pink_ring_2 = ImageTk.PhotoImage(self.jwe_pink_2)
        self.jwe_pink = Image.open("jwellery/1.1e粉紅鑽.png").resize((105,80))
        self.pink_ring = ImageTk.PhotoImage(self.jwe_pink)
        can_pink_ring = self.canvas.create_image(625, 310, image=self.pink_ring, anchor='n')
        self.canvas.tag_bind(can_pink_ring, "<Button-1>", lambda e:[self.put_item(can_pink_ring, 7)])

        self.jwe_spinel_2 = Image.open("jwellery/尖晶石.png").resize((50,50))
        self.spinel_2 = ImageTk.PhotoImage(self.jwe_spinel_2)
        self.jwe_spinel = Image.open("jwellery/尖晶石.png").resize((50,60))
        self.spinel = ImageTk.PhotoImage(self.jwe_spinel)
        can_spinel = self.canvas.create_image(55, 70, image=self.spinel, anchor='n')
        self.canvas.tag_bind(can_spinel, "<Button-1>", lambda e:[self.put_item(can_spinel, 8)])

        self.jwe_ruby_rect_2 = Image.open("jwellery/紅寶石3.png").resize((50,50))
        self.ruby_rect_2 = ImageTk.PhotoImage(self.jwe_ruby_rect_2)
        self.jwe_ruby_rect = Image.open("jwellery/紅寶石3.png").resize((40,40))
        self.ruby_rect = ImageTk.PhotoImage(self.jwe_ruby_rect)
        can_ruby_rect = self.canvas.create_image(1100, 215, image=self.ruby_rect, anchor='n')
        self.canvas.tag_bind(can_ruby_rect, "<Button-1>", lambda e:[self.put_item(can_ruby_rect, 9)])

        self.jwe_glass_ball_2 = Image.open("jwellery/玻璃球.png").resize((50,50))
        self.glass_ball_2 = ImageTk.PhotoImage(self.jwe_glass_ball_2)
        self.jwe_glass_ball = Image.open("jwellery/玻璃球.png").resize((150,150))
        self.glass_ball = ImageTk.PhotoImage(self.jwe_glass_ball)
        can_glass_ball = self.canvas.create_image(1015, 535, image=self.glass_ball, anchor='n')
        self.canvas.tag_bind(can_glass_ball, "<Button-1>", lambda e:[self.put_item(can_glass_ball, 10)])

        self.jwe_emerald_sqr_2 = Image.open("jwellery/祖母綠2.png").resize((50,50))
        self.emerald_sqr_2 = ImageTk.PhotoImage(self.jwe_emerald_sqr_2)
        self.jwe_emerald_sqr = Image.open("jwellery/祖母綠2.png").resize((25,25))
        self.emerald_sqr = ImageTk.PhotoImage(self.jwe_emerald_sqr)
        can_emerald_sqr = self.canvas.create_image(230, 365, image=self.emerald_sqr, anchor='n')
        self.canvas.tag_bind(can_emerald_sqr, "<Button-1>", lambda e:[self.put_item(can_emerald_sqr, 11)])

        self.jwe_pearl_2 = Image.open("jwellery/珍珠.png").resize((50,50))
        self.pearl_2 = ImageTk.PhotoImage(self.jwe_pearl_2)
        self.jwe_pearl = Image.open("jwellery/珍珠.png").resize((100,50))
        self.pearl = ImageTk.PhotoImage(self.jwe_pearl)
        can_pearl = self.canvas.create_image(730, 560, image=self.pearl, anchor='n')
        self.canvas.tag_bind(can_pearl, "<Button-1>", lambda e:[self.put_item(can_pearl, 12)])

        self.jwe_sapphire_round_2 = Image.open("jwellery/藍寶石2.png").resize((50,50))
        self.sapphire_round_2 = ImageTk.PhotoImage(self.jwe_sapphire_round_2)
        self.jwe_sapphire_round = Image.open("jwellery/藍寶石2.png").resize((25,25))
        self.sapphire_round = ImageTk.PhotoImage(self.jwe_sapphire_round)
        can_sapphire_round = self.canvas.create_image(785, 175, image=self.sapphire_round, anchor='n')
        self.canvas.tag_bind(can_sapphire_round, "<Button-1>", lambda e:[self.put_item(can_sapphire_round, 13)])

        self.jwe_rubellite_2 = Image.open("jwellery/紅碧璽.png").resize((50,50))
        self.rubellite_2 = ImageTk.PhotoImage(self.jwe_rubellite_2)
        self.jwe_rubellite = Image.open("jwellery/紅碧璽.png").resize((30,20))
        self.rubellite = ImageTk.PhotoImage(self.jwe_rubellite)
        can_rubellite = self.canvas.create_image(390, 235, image=self.rubellite, anchor='n')
        self.canvas.tag_bind(can_rubellite, "<Button-1>", lambda e:[self.put_item(can_rubellite, 14)])

        self.jwe_grandidierite_2 = Image.open("jwellery/硅硼鎂鋁石.png").resize((50,50))
        self.grandidierite_2 = ImageTk.PhotoImage(self.jwe_grandidierite_2)
        self.jwe_grandidierite = Image.open("jwellery/硅硼鎂鋁石.png").resize((30,25))
        self.grandidierite = ImageTk.PhotoImage(self.jwe_grandidierite)
        can_grandidierite = self.canvas.create_image(860, 365, image=self.grandidierite, anchor='n')
        self.canvas.tag_bind(can_grandidierite, "<Button-1>", lambda e:[self.put_item(can_grandidierite, 15)])

        self.jwe_moissanite_2 = Image.open("jwellery/莫桑石.png").resize((50,50))
        self.moissanite_2 = ImageTk.PhotoImage(self.jwe_moissanite_2)
        self.jwe_moissanite = Image.open("jwellery/莫桑石.png").resize((30,30))
        self.moissanite = ImageTk.PhotoImage(self.jwe_moissanite)
        can_moissanite = self.canvas.create_image(330, 70, image=self.moissanite, anchor='n')
        self.canvas.tag_bind(can_moissanite, "<Button-1>", lambda e:[self.put_item(can_moissanite, 16)])
        
        self.jwe_opal_2 = Image.open("jwellery/蛋白石.png").resize((50,50))
        self.opal_2 = ImageTk.PhotoImage(self.jwe_opal_2)
        self.jwe_opal = Image.open("jwellery/蛋白石.png").resize((50,50))
        self.opal = ImageTk.PhotoImage(self.jwe_opal)
        can_opal = self.canvas.create_image(360, 580, image=self.opal, anchor='n')
        self.canvas.tag_bind(can_opal, "<Button-1>", lambda e:[self.put_item(can_opal, 17)])

        self.jwe_amethyst_2 = Image.open("jwellery/紫水晶.png").resize((50,50))
        self.amethyst_2 = ImageTk.PhotoImage(self.jwe_amethyst_2)
        self.jwe_amethyst = Image.open("jwellery/紫水晶.png").resize((50,50))
        self.amethyst = ImageTk.PhotoImage(self.jwe_amethyst)
        can_amethyst = self.canvas.create_image(1020, 360, image=self.amethyst, anchor='n')
        self.canvas.tag_bind(can_amethyst, "<Button-1>", lambda e:[self.put_item(can_amethyst, 18)])

        self.jwe_chrysoberyl_cat_2 = Image.open("jwellery/貓眼石.png").resize((50,50))
        self.chrysoberyl_cat_2 = ImageTk.PhotoImage(self.jwe_chrysoberyl_cat_2)
        self.jwe_chrysoberyl_cat = Image.open("jwellery/貓眼石.png").resize((55,45))
        self.chrysoberyl_cat = ImageTk.PhotoImage(self.jwe_chrysoberyl_cat)
        can_chrysoberyl_cat = self.canvas.create_image(550, 470, image=self.chrysoberyl_cat, anchor='n')
        self.canvas.tag_bind(can_chrysoberyl_cat, "<Button-1>", lambda e:[self.put_item(can_chrysoberyl_cat, 19)])

        self.jwe_jade_2 = Image.open("jwellery/dragon jade.png").resize((50,50))
        self.jade_2 = ImageTk.PhotoImage(self.jwe_jade_2)
        self.jwe_jade = Image.open("jwellery/dragon jade.png").resize((20,20))
        self.jade = ImageTk.PhotoImage(self.jwe_jade)
        can_jade = self.canvas.create_image(900, 180, image=self.jade, anchor='n')
        self.canvas.tag_bind(can_jade, "<Button-1>", lambda e:[self.put_item(can_jade, 20)])
        
         # 對話框
        self.show_info("做搶匪也不能貪心，最多只能拿八個。")
		

    # 撿寶石，放進道具欄
    def put_item(self, pic, para):
        coordinates = [[130, 185], [130, 260], [130, 335], [130, 410], 
                       [55, 185], [55, 260], [55, 335], [55, 410]]
        self.pics_in_bag.append(para)
        print(len(self.pics_in_bag), self.pics_in_bag)

        if len(self.pics_in_bag) <= 8:
            for i in range(len(self.pics_in_bag)):
                if self.pics_in_bag[i] == 1:
                    self.canvas.create_image(coordinates[i][0], coordinates[i][1], image=self.expensive_paint1)
                    self.total_value += 96700
                elif self.pics_in_bag[i] == 2:
                    self.canvas.create_image(coordinates[i][0], coordinates[i][1], image=self.expensive_statue1)
                    self.total_value += 18400
                elif self.pics_in_bag[i] == 3:
                    self.canvas.create_image(coordinates[i][0], coordinates[i][1], image=self.expensive_human_statue1)
                    self.total_value += 45500
                elif self.pics_in_bag[i] == 4:
                    self.canvas.create_image(coordinates[i][0], coordinates[i][1], image=self.expensive_vegetable1)
                    self.total_value += 30000
                elif self.pics_in_bag[i] == 5:
                    self.canvas.create_image(coordinates[i][0], coordinates[i][1], image=self.expensive_vast1)
                    self.total_value += 55300
                elif self.pics_in_bag[i] == 6:
                    self.canvas.create_image(coordinates[i][0], coordinates[i][1], image=self.gold_2)
                    self.total_value += 50000
                elif self.pics_in_bag[i] == 7:
                    self.canvas.create_image(coordinates[i][0], coordinates[i][1], image=self.pink_ring_2)
                    self.total_value += 110000000
                elif self.pics_in_bag[i] == 8:
                    self.canvas.create_image(coordinates[i][0], coordinates[i][1], image=self.spinel_2)
                    self.total_value += 20000
                elif self.pics_in_bag[i] == 9:
                    self.canvas.create_image(coordinates[i][0], coordinates[i][1], image=self.ruby_rect_2)
                    self.total_value += 2000000
                elif self.pics_in_bag[i] == 10:
                    self.canvas.create_image(coordinates[i][0], coordinates[i][1], image=self.glass_ball_2)
                    self.total_value += 40
                elif self.pics_in_bag[i] == 11:
                    self.canvas.create_image(coordinates[i][0], coordinates[i][1], image=self.emerald_sqr_2)
                    self.total_value += 2600000
                elif self.pics_in_bag[i] == 12:
                    self.canvas.create_image(coordinates[i][0], coordinates[i][1], image=self.pearl_2)
                    self.total_value += 3000000000
                elif self.pics_in_bag[i] == 13:
                    self.canvas.create_image(coordinates[i][0], coordinates[i][1], image=self.sapphire_round_2)
                    self.total_value += 3000000
                elif self.pics_in_bag[i] == 14:
                    self.canvas.create_image(coordinates[i][0], coordinates[i][1], image=self.rubellite_2)
                    self.total_value += 1200
                elif self.pics_in_bag[i] == 15:
                    self.canvas.create_image(coordinates[i][0], coordinates[i][1], image=self.grandidierite_2)
                    self.total_value += 20000
                elif self.pics_in_bag[i] == 16:
                    self.canvas.create_image(coordinates[i][0], coordinates[i][1], image=self.moissanite_2)
                    self.total_value += 4500
                elif self.pics_in_bag[i] == 17:
                    self.canvas.create_image(coordinates[i][0], coordinates[i][1], image=self.opal_2)
                    self.total_value += 100000
                elif self.pics_in_bag[i] == 18:
                    self.canvas.create_image(coordinates[i][0], coordinates[i][1], image=self.amethyst_2)
                    self.total_value += 300
                elif self.pics_in_bag[i] == 19:
                    self.canvas.create_image(coordinates[i][0], coordinates[i][1], image=self.chrysoberyl_cat_2)
                    self.total_value += 10000000
                elif self.pics_in_bag[i] == 20:
                    self.canvas.create_image(coordinates[i][0], coordinates[i][1], image=self.jade_2)
                    self.total_value += 6900
            self.canvas.delete(pic)

            # 拿滿八個寶物
        if len(self.pics_in_bag) == 8:
            # 放對話框
            self.dlg3 = Image.open("對話框.png")
            self.dlg3 = self.dlg3.resize((1000,550))
            self.dlg3 = ImageTk.PhotoImage(self.dlg3)
            dlg3 = self.canvas.create_image(624,310, image=self.dlg3, anchor='n')
            self.canvas.tag_raise(self.dlg3)
            # 放對話
            text3 = self.canvas.create_text(628,580,
                        text = "拿滿八個囉，是時候閃人啦٩(˃̶͈̀௰˂̶͈́)و",
                        font = (False, 20), 
                        fill = "white",
                        anchor = "n")
            #放返回鍵
            self.re_button = Image.open("回主畫面.png")
            self.re_button = self.re_button.resize((50,50))
            self.re_button = ImageTk.PhotoImage(self.re_button)
            re_button = self.canvas.create_image(1000, 630, image = self.re_button)
            self.canvas.tag_bind(re_button,"<Button-1>",
			    lambda e:[self.canvas.delete(re_button),self.canvas.delete(dlg3),self.canvas.delete(text3), self.EndVideoPlay()])
    
    def EndVideoPlay(self):
            self.label.after(1000 , lambda: self.label.destroy())  # 計時器消失
            cap2 = cv2.VideoCapture('Cutscenes_reverse!.mp4')
            while(cap2.isOpened()):
                ret, frame = cap2.read()
                time.sleep(0.02)  # 播放倍速
                if ret == False:
                    break
                cv2.imshow('frame',frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            cap2.release()
            cv2.destroyAllWindows()

            # 最後逃出大樓畫面
            self.back3 = Image.open('building.jpg')
            self.back3 = self.back3.resize((1248, 702))
            self.back3 = ImageTk.PhotoImage(self.back3)
            self.canvas.create_image(0,0, image=self.back3, anchor='nw')

            # 計算分數
            self.sc = Image.open('final.png')
            self.sc = self.sc.resize((1100, 600))
            self.sc = ImageTk.PhotoImage(self.sc)
            self.canvas.create_image(624,351, image=self.sc, anchor='center')
            self.canvas.create_text(900,485,text = self.total_value, font = (False, 60), fill = "white")
    
    # 對話框
    def show_info(self, info):
        # 放對話框
        self.dlg = Image.open("對話框.png")
        self.dlg = self.dlg.resize((1000,550))
        self.dlg = ImageTk.PhotoImage(self.dlg)
        dlg = self.canvas.create_image(624,310, image=self.dlg, anchor='n')

         #放對話框
        text = self.canvas.create_text(628,580,
                   text = info,
                   font = (False, 20), 
                   fill = "white",
                   anchor = "n")
        #放返回鍵
        self.re_button = Image.open("回主畫面.png")
        self.re_button = self.re_button.resize((50,50))
        self.re_button = ImageTk.PhotoImage(self.re_button)
        re_button = self.canvas.create_image(1000, 630, image = self.re_button)
        self.canvas.tag_bind(re_button,"<Button-1>",
		    lambda e:[self.canvas.delete(re_button),self.canvas.delete(dlg),self.canvas.delete(text)])

    # 倒數計時器
    def countdown(self, remaining = None, sprec = None):
        if remaining is not None:
            self.remaining = remaining

        if sprec is not None:
            self.sprec = sprec

        # 時間到game over
        if self.remaining <= 0 and self.issecond == False:
            self.label.configure(text="Time's Up!", width=8)
            self.label.after(1000 , lambda: self.label.destroy())  # 計時器消失
            #self.label.after(1000 , self.label.master.destroy)  # 視窗關閉
            self.img = Image.open('game over.png')
            self.img = self.img.resize((1100, 600))
            self.img = ImageTk.PhotoImage(self.img)
            self.canvas.create_image(624,351, image=self.img, anchor='center')
            self.im = Image.open('逮捕.png')
            self.im = self.im.resize((350, 250))
            self.im = ImageTk.PhotoImage(self.im)
            self.canvas.create_image(100,650, image=self.im, anchor='sw')

        # 時間到 闖關成功影片
        elif self.remaining == 0 and self.issecond == True:
            self.label.configure(text="Time's Up!", width=8)
            self.label.after(1000 , lambda: self.label.destroy())  # 計時器消失
            cap2 = cv2.VideoCapture('Cutscenes_reverse!.mp4')
            while(cap2.isOpened()):
              ret, frame = cap2.read()
              time.sleep(0.02)  # 播放倍速
              if ret == False:
                break
              cv2.imshow('frame',frame)
              if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            cap2.release()
            cv2.destroyAllWindows()
            
            # 最後逃出大樓畫面
            self.back3 = Image.open('building.jpg')
            self.back3 = self.back3.resize((1248, 702))
            self.back3 = ImageTk.PhotoImage(self.back3)
            self.canvas.create_image(0,0, image=self.back3, anchor='nw')
            
            # 計算分數
            self.sc = Image.open('final.png')
            self.sc = self.sc.resize((1100, 600))
            self.sc = ImageTk.PhotoImage(self.sc)
            self.canvas.create_image(624,351, image=self.sc, anchor='center')
            self.canvas.create_text(900,485,text = self.total_value, font = (False, 30), fill = "white")


        elif self.sprec == 0:
            self.label.configure(text="%02d:%02d" % (self.remaining/60,self.remaining%60))
            self.label.place(x = 1120, y = 20)
            self.remaining = self.remaining - 60
            self.sprec += 1
            self.after(1000, self.countdown)

        elif self.sprec == 1:
            self.label.configure(text="%02d:%02d" % (self.remaining/60,self.remaining%60))
            self.label.place(x = 1120, y = 20)
            self.remaining = self.remaining - 1
            self.after(2000, self.countdown)

        else:
            self.label.configure(text="%02d:%02d" % (self.remaining/60,self.remaining%60))
            self.label.place(x = 1120, y = 20)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)

class locked_clock(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self)
		self.master = master
		self.createWidgets()
		self.no_key = False
		# self.config(bg="red")
		self.check_password()
		
	def Destroy(self):
		self.destroy()
		self.master.canvas.delete(self.master.locked_clock)

	def createWidgets(self):
    	# 設定字型
		f1 = tkFont.Font (size = 48, family = "Courier New")
		f2 = tkFont.Font (size = 32, family = "Courier New")
		
		# 放時鐘
		self.clock2 = Image.open("時鐘.png")
		self.clock2 = self.clock2.resize((300, 300))
		self.clock2 = ImageTk.PhotoImage(self.clock2)
		self.c1ock2 = tk.Label(self, image=self.clock2)
		
        # 設定按鈕
		self.lblNum = tk.Label(self, text = "", height = 1, width = 7, font = f1)
		self.btnNum1 = tk.Button(self, text = "1", command = self.clickBtnNum1, height = 1, width = 2, font = f2)
		self.btnNum2 = tk.Button(self, text = "2", command = self.clickBtnNum2, height = 1, width = 2, font = f2)
		self.btnNum3 = tk.Button(self, text = "3", command = self.clickBtnNum3, height = 1, width = 2, font = f2)
		self.btnNum4 = tk.Button(self, text = "4", command = self.clickBtnNum4, height = 1, width = 2, font = f2)
		self.btnNum5 = tk.Button(self, text = "5", command = self.clickBtnNum5, height = 1, width = 2, font = f2)
		self.btnNum6 = tk.Button(self, text = "6", command = self.clickBtnNum6, height = 1, width = 2, font = f2)
		self.btnNum7 = tk.Button(self, text = "7", command = self.clickBtnNum7, height = 1, width = 2, font = f2)
		self.btnNum8 = tk.Button(self, text = "8", command = self.clickBtnNum8, height = 1, width = 2, font = f2)
		self.btnNum9 = tk.Button(self, text = "9", command = self.clickBtnNum9, height = 1, width = 2, font = f2)
		self.btnClose = tk.Button(self, text = "x", command = self.Destroy, height = 1, width = 2, font = f2)
		
		# 設定位置
		self.c1ock2.grid(row = 0, column = 0, columnspan=5)
		self.lblNum.grid(row = 1, column = 0, columnspan = 5)
		self.btnNum1.grid(row = 2, column = 0, sticky = tk.W)
		self.btnNum2.grid(row = 2, column = 1, sticky = tk.W)	
		self.btnNum3.grid(row = 2, column = 2, sticky = tk.W)
		self.btnNum4.grid(row = 2, column = 3, sticky = tk.W)
		self.btnNum5.grid(row = 2, column = 4, sticky = tk.W)
		self.btnNum6.grid(row = 3, column = 0, sticky = tk.W)
		self.btnNum7.grid(row = 3, column = 1, sticky = tk.W)
		self.btnNum8.grid(row = 3, column = 2, sticky = tk.W)
		self.btnNum9.grid(row = 3, column = 3, sticky = tk.W)		
		self.btnClose.grid(row = 3, column = 4, sticky = tk.W)

	def check_password(self):  # 檢查密碼是否正確
		temp = self.lblNum.cget("text")
		if temp == "6473":
			password = True
			print("got it")  # 切換圖片
			self.Destroy()
			open_clock(self.master)

	def clean_password(self):  # 清除密碼
		try:
			temp = self.lblNum.cget("text")
		except:
			temp = ""
		if len(temp) >= 5:
			self.lblNum.configure(text = self.lblNum.cget("text")[-1])
		
	def clickBtnNum1(self):
		self.lblNum.configure(text = self.lblNum.cget("text") + "1")
		self.check_password()
		self.clean_password()
	
	def clickBtnNum2(self):
		self.lblNum.configure(text = self.lblNum.cget("text") + "2")
		self.check_password()
		self.clean_password()
	
	def clickBtnNum3(self):
		self.lblNum.configure(text = self.lblNum.cget("text") + "3")
		self.check_password()
		self.clean_password()
	
	def clickBtnNum4(self):
		self.lblNum.configure(text = self.lblNum.cget("text") + "4")
		self.check_password()
		self.clean_password()
	
	def clickBtnNum5(self):
		self.lblNum.configure(text = self.lblNum.cget("text") + "5")
		self.check_password()
		self.clean_password()
	
	def clickBtnNum6(self):
		self.lblNum.configure(text = self.lblNum.cget("text") + "6")
		self.check_password()
		self.clean_password()
	
	def clickBtnNum7(self):
		self.lblNum.configure(text = self.lblNum.cget("text") + "7")
		self.check_password()
		self.clean_password()
	
	def clickBtnNum8(self):
		self.lblNum.configure(text = self.lblNum.cget("text") + "8")
		self.check_password()
		self.clean_password()
	
	def clickBtnNum9(self):
		self.lblNum.configure(text = self.lblNum.cget("text") + "9")
		self.check_password()
		self.clean_password()
	
class open_clock(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self)
		self.master = master
		self.createWidgets()
		self.master.config(bg='blue')
		self.master.open_clock = self.master.canvas.create_window(400,50, anchor="nw", window = self, width = 380, height = 600)
		self.createWidgets()

	def createWidgets(self):
		# 放打開的時鐘
		self.clock3 = Image.open("打開的時鐘.png").resize((350, 350))
		self.clock3 = ImageTk.PhotoImage(self.clock3)
		self.c1ock3 = tk.Label(self, image=self.clock3)
		self.c1ock3.grid(row = 0, column = 0, columnspan=5)
		
		# 放鑰匙
		# if self.no_key == False:
		self.clock2 = Image.open("key.png")
		self.clock2 = self.clock2.resize((100, 100))
		self.clock2 = ImageTk.PhotoImage(self.clock2)
		self.done = tk.Button(self, image=self.clock2, command=self.get_key)
		self.done.grid(row = 1, column = 0, columnspan=5)
		
		# 放按鈕
		f1 = tkFont.Font (size = 20, family = "Courier New")
		self.btn_back = tk.Button(self,text='恭喜你成功解鎖\n獲得鑰匙',command=self.back, font=f1)
		self.btn_back.grid(row = 2, column = 2)

	def back(self):
		self.destroy()
		self.master.canvas.delete(self.master.open_clock)
	
	def get_key(self):
		self.getKey = Image.open("key.png")
		self.getKey = self.getKey.resize((40,40))
		self.getKey = ImageTk.PhotoImage(self.getKey)
		self.master.getKey = self.master.canvas.create_image(65,195,image = self.getKey)
		self.master.canvas.tag_bind(self.master.door, "<Button-1>", lambda e:[self.master.video_play(), self.master.second()])
		self.no_key = True
		self.done.destroy()


app = ExampleApp()
app.mainloop()
