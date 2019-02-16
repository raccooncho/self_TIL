
# 아래에 코드를 작성해주세요.
import random

class Pokemon:

    def __init__(self, name, level, element):
        elements = ['elec', 'water', 'fire', 'leef']
        element_attacks = ['10만 볼트', '물 대 포', '화염 방사', '잎날가르기']
        status_attacks = ['전기자석파', '냉 동 빔', '도깨비 불', '씨 뿌리기']
        status = ['nomal', '마비', '동상', '화상', '흡수']
        self.accuracy_rate = [1, 1, 2, 2, 2, 2, 2, 2, 3, 3]
        self.name = name
        self.exp = 0
        self.level = level
        self.HP = level * 10
        self.HP_p_level = 10
        self.vapp = 10
        self.sapp = 3
        self.speed = level * 2
        self.attack = level * 1.5
        self.ammor = level * 0.5
        self.element = elements.index(element)  # 속성에 부여한 임의 코드(int)
        self.e_attack = element_attacks[self.element]
        self.s_attack = status_attacks[self.element]
        self.s_attack_s = status[self.element+1]
        self.status = 'nomal'
        self.attack_num = 1
        self.speed_d = [1, 2, 2]
        if self.element == 0:
            self.speed = level * 2.5
            self.accuracy_rate = [1, 1, 1, 2, 2, 2, 2, 2, 2, 3]
            self.speed_d = [1, 2]
            self.HP = level * 8
            self.HP_p_level = 8
        elif self.element == 1:
            self.ammor = level * 1
            self.attack = round(level * 1.2)
        elif self.element == 2:
            self.ammor = round(level * 0.2)
            self.attack = level * 2
        else:
            self.speed = level * 1.5
            self.HP = level * 15
            self.accuracy_rate = [1, 2, 2, 2, 2, 2, 2, 3, 3, 3]
            self.speed_d = [1, 2, 2, 2]
            self.HP_p_level = 15
        self.max_hp = self.HP
        self.heal_speed = self.speed
        self.max_vapp = self.vapp
        self.max_sapp = self.sapp

    def levelup(self):
        if self.exp >= self.level:
            while self.exp >= self.level:
                self.exp -= self.level
                self.level += 1
                self.max_hp = self.level * 10
                self.HP_p_level = 10
                self.speed = self.level * 2
                self.attack = self.level * 1.5
                self.ammor = self.level * 0.5
                if self.element == 0:
                    self.speed = self.level * 2.5
                    self.max_hp = self.level * 8
                elif self.element == 1:
                    self.ammor = self.level * 1
                    self.attack = round(self.level * 1.2)
                elif self.element == 2:
                    self.ammor = round(self.level * 0.2)
                    self.attack = self.level * 2
                else:
                    self.speed = self.level * 1.5
                    self.max_hp = self.level * 15
                self.heal_speed = self.speed
            return 1
        else:
            return 0

    def batttle_exp(self, enemy):
        self.exp += enemy.level

    def set_HP(self, point):
        self.HP += point

    def light_heal(self):
        print(f'$$ 출시 기념 이벤트 $$')
        input()
        print(f'{self.name}의 레벨 업을 축하하는 의미로 체력과 상태이상을 회복시켜 드립니다!')
        input()
        self.HP = self.max_hp
        self.status = 'nomal'
    
    def full_heal(self):
        print(f'조너굴님의 축복으로 {self.name}의 모든 상태가 완전히 치료되었습니다~!')
        input()
        self.HP = self.max_hp
        self.status = 'nomal'
        self.vapp = self.max_vapp
        self.sapp = self.max_sapp

    def check_status(self):
        if self.HP <= 0:
            return False
        else:
            return self.HP

    def attack_rate(self, enemy):
        return self.attack / (self.attack + enemy.ammor)
   
    def speed_down(self):
        speeddown = random.choice(self.speed_d)
        if speeddown == 1:
            self.speed -= 1
            print(f'{self.name}는 기술을 시도하느라 지쳐서 스피드가 1 떨어졌다.')
            input()
    
    def n_attack_motion(self, enemy, n):
        enemy.set_HP(-round(self.attack * n * self.attack_rate(enemy)))
        print(f'{round(self.attack * n * self.attack_rate(enemy))}의 데미지를 주었다.')
        input()

    def e_attack_motion(self, enemy, n):
        print(f'{round(self.attack * n * self.attack_rate(enemy))}의 데미지를 주었다.')
        input()
        self.speed_down()
        enemy.set_HP(-round(self.attack * n * self.attack_rate(enemy)))
        self.vapp -= 1

    def s_attack_motion(self, enemy, n):
        print(f'{round(self.attack * n * self.attack_rate(enemy))}의 데미지를 주었다.')
        input()
        self.speed_down()
        print(f'{enemy.name}는 {self.s_attack_s}상태에 걸렸다.')
        input()
        enemy.set_HP(-round(self.attack * n * self.attack_rate(enemy)))
        self.sapp -= 1

    def body_attack(self, enemy):
        print(f'{self.name}가 {enemy.name}에게 몸통박치기를 시도하였다.')
        input()
        attack_accuracy = random.choice(self.accuracy_rate)
        if attack_accuracy == 1:
            print('급소에 명중했다!')
            input()
            self.n_attack_motion(enemy, 2)
        elif attack_accuracy == 3:
            print(f'{self.name}의 공격이 빗나갔다.')
            input()
            print('아무일도 일어나지 않았다.')
            input()
        else:
            self.n_attack_motion(enemy, 1)
    
    def e_attack_uneffective(self, enemy):
        print(f'{self.name}가 {enemy.name}에게 {self.e_attack}를(을) 시도하였다.')
        input()
        attack_accuracy = random.choice(self.accuracy_rate)
        if attack_accuracy == 1:
            if self.vapp > 0:
                print('효과가 부족했다.')
                input()
                print('급소에 명중했다!')
                input()
                self.e_attack_motion(enemy, 2)
            else:
                print(f'{self.name}는 pp가 부족하여 더 이상 {self.e_attack}를(을) 사용할 수 없다.')
                input()
                print('대신 몸통 박치기를 하였다.')
                input()
                print('급소에 명중했다!')
                input()
                self.n_attack_motion(enemy, 2)
        elif attack_accuracy == 2:
            if self.vapp > 0:
                print('효과가 부족했다.')
                input()
                self.e_attack_motion(enemy, 1)
            else:
                print(f'{self.name}는 pp가 부족하여 더 이상 {self.e_attack}를(을) 사용할 수 없다.')
                input()
                print('대신 몸통 박치기를 하였다.')
                input()
                self.n_attack_motion(enemy, 1)
        else:
            print(f'{self.name}의 공격이 빗나갔다.')
            self.vapp -= 1
            input()
            print('아무일도 일어나지 않았다.') 
            input()

    def e_attack_normal(self, enemy):
        print(f'{self.name}가 {enemy.name}에게 {self.e_attack}를(을) 시도하였다.')
        input()
        attack_accuracy = random.choice(self.accuracy_rate)
        if attack_accuracy == 1:
            if self.vapp > 0:
                print('급소에 명중했다!')
                input()
                self.e_attack_motion(enemy, 4)
            else:
                print(f'{self.name}는 pp가 부족하여 더 이상 {self.e_attack}를(을) 사용할 수 없다.')
                input()
                print('대신 몸통 박치기를 하였다.')
                input()
                print('급소에 명중했다!')
                input()
                self.n_attack_motion(enemy, 2)
        elif attack_accuracy == 2:
            if self.vapp > 0:
                self.e_attack_motion(enemy, 2)
            else:
                print(f'{self.name}는 pp가 부족하여 더 이상 {self.e_attack}를(을) 사용할 수 없다.')
                input()
                print('대신 몸통 박치기를 하였다.')
                input()
                self.n_attack_motion(enemy, 1)
        else:
            print(f'{self.name}의 공격이 빗나갔다.')
            self.vapp -= 1
            input()
            print('아무일도 일어나지 않았다.') 
            input()

    def e_attack_effective(self, enemy): 
        print(f'{self.name}가 {enemy.name}에게 {self.e_attack}를(을) 시도하였다.')
        input()
        attack_accuracy = random.choice(self.accuracy_rate)
        if attack_accuracy == 1:
            if self.vapp > 0:
                print('효과가 굉장했다.')
                input()
                print('급소에 명중했다!')
                input()
                self.e_attack_motion(enemy, 8)
            else:
                print(f'{self.name}는 pp가 부족하여 더 이상 {self.e_attack}를(을) 사용할 수 없다.')
                input()
                print('대신 몸통 박치기를 하였다.')
                input()
                print('급소에 명중했다!')
                input()
                self.n_attack_motion(enemy, 2)
        elif attack_accuracy == 2:
            if self.vapp > 0:
                print(f'효과가 굉장했다.')
                input()
                self.e_attack_motion(enemy, 4)
            else:
                print(f'{self.name}는 pp가 부족하여 더 이상 {self.e_attack}를(을) 사용할 수 없다.')
                input()
                print(f'대신 몸통 박치기를 하였다.')
                input()
                self.n_attack_motion(enemy, 1)
        else:
            print(f'{self.name}의 공격이 빗나갔다.')
            self.vapp -= 1
            input()
            print('아무일도 일어나지 않았다.') 
            input()

    def element_attack(self, enemy):
        if self.element == enemy.element + 1 or (self.element == 1 and enemy.element == 3):
            self.e_attack_uneffective(enemy)
        elif self.element == enemy.element - 1 or (self.element == 3 and enemy.element == 1):
            self.e_attack_effective(enemy)
        else:
            self.e_attack_normal(enemy)
    
    def s_attack_uneffective(self, enemy):
        print(f'{self.name}가 {enemy.name}에게 {self.s_attack}를(을) 시도하였다.')
        input()
        attack_accuracy = random.choice(self.accuracy_rate)
        if attack_accuracy == 1:
            if self.sapp > 0:
                print('효과가 부족했다.')
                input()
                print('급소에 명중했다!')
                input()
                self.s_attack_motion(enemy, 1)
                enemy.status = self.s_attack_s
            else:
                print(f'{self.name}는 pp가 부족하여 더 이상 {self.s_attack}를(을) 사용할 수 없다.')
                input()
                print('대신 몸통 박치기를 하였다.')
                input()
                print('급소에 명중했다!')
                input()
                self.n_attack_motion(enemy, 2)
        elif attack_accuracy == 2:
            if self.sapp > 0:
                print('효과가 부족했다.')
                input()
                self.s_attack_motion(enemy, 0.5)
                enemy.status = self.s_attack_s
            else:
                print(f'{self.name}는 pp가 부족하여 더 이상 {self.s_attack}를(을) 사용할 수 없다.')
                input()
                print('대신 몸통 박치기를 하였다.')
                input()
                self.n_attack_motion(enemy, 1)
        else:
            print(f'{self.name}의 공격이 빗나갔다.')
            self.sapp -= 1
            input()
            print('아무일도 일어나지 않았다.') 
            input()
        
    def s_attack_normal(self, enemy):
        print(f'{self.name}가 {enemy.name}에게 {self.s_attack}를(을) 시도하였다.')
        input()
        attack_accuracy = random.choice(self.accuracy_rate)
        if attack_accuracy == 1:
            if self.sapp > 0:
                print('급소에 명중했다!')
                input()
                self.s_attack_motion(enemy, 2)
                enemy.status = self.s_attack_s
            else:
                print(f'{self.name}는 pp가 부족하여 더 이상 {self.s_attack}를(을) 사용할 수 없다.')
                input()
                print('대신 몸통 박치기를 하였다.')
                input()
                print('급소에 명중했다!')
                input()
                self.n_attack_motion(enemy, 2)
        elif attack_accuracy == 2:
            if self.sapp > 0:
                self.s_attack_motion(enemy, 1)
                enemy.status = self.s_attack_s
            else:
                print(f'{self.name}는 pp가 부족하여 더 이상 {self.s_attack}를(을) 사용할 수 없다.')
                input()
                print('대신 몸통 박치기를 하였다.')
                input()
                self.n_attack_motion(enemy, 1)
        else:
            print(f'{self.name}의 공격이 빗나갔다.')
            self.sapp -= 1
            input()
            print('아무일도 일어나지 않았다.') 
            input()
    
    def s_attack_effective(self, enemy):
        print(f'{self.name}가 {enemy.name}에게 {self.s_attack}를(을) 시도하였다.')
        input()
        attack_accuracy = random.choice(self.accuracy_rate)
        if attack_accuracy == 1:
            if self.sapp > 0:
                print('효과가 굉장했다.')
                input()
                print('급소에 명중했다!')
                input()
                self.s_attack_motion(enemy, 4)
                enemy.status = self.s_attack_s
            else:
                print(f'{self.name}는 pp가 부족하여 더 이상 {self.s_attack}를(을) 사용할 수 없다.')
                input()
                print('대신 몸통 박치기를 하였다.')
                input()
                print('급소에 명중했다!')
                input()
                self.n_attack_motion(enemy, 2)
        elif attack_accuracy == 2:
            if self.sapp > 0:
                print('효과가 굉장했다.')
                input()
                self.s_attack_motion(enemy, 2)
                enemy.status = self.s_attack_s
            else:
                print(f'{self.name}는 pp가 부족하여 더 이상 {self.s_attack}를(을) 사용할 수 없다.')
                input()
                print('대신 몸통 박치기를 하였다.')
                input()
                self.n_attack_motion(enemy, 1)
        else:
            print(f'{self.name}의 공격이 빗나갔다.')
            self.sapp -= 1
            input()
            print('아무일도 일어나지 않았다.') 
            input()
   
    def status_attack(self, enemy):
        if self.element == enemy.element + 1:
            self.s_attack_uneffective(enemy)
        elif self.element == enemy.element -1 or (self.element * enemy.element == 3):
            self.s_attack_effective(enemy)
        else:
            self.s_attack_normal(enemy)
    
    def status_motion(self, enemy):
        if self.status == '마비':
            print(f'{self.name}는 마비되어 움직이기 힘들다.')
            input()
        elif self.status == '동상':
            fcount = [1, 2, 2, 2]
            if random.choice(fcount) == 2:
                print(f'{self.name}는 동상에 걸려 움직일 수 없다.')
                input()        
            else:
                self.status = 'nomal'
                print(f'{self.name}의 동상이 풀렸다.')
                input()
        elif self.status == '화상':
            print(f'{self.name}는 화상에 걸려 {enemy.attack}의 데미지를 입었다.')
            input()
            self.HP -= enemy.attack
        elif self.status == '흡수':
            print(f'{enemy.name}는 {self.name}의 체력을 {enemy.attack * 0.5}만큼 흡수했다. ')
            input()
            self.HP -= enemy.attack * 0.5
            enemy.HP += enemy.attack * 0.5
    
    def pal_effect(self, enemy):
        chance = random.choice([1, 2])
        if chance == 1:
            print(f'{self.name}는 몸이 저릿저릿 해서 공격에 실패했다.')
            input()
        else: 
            self.battle_order(enemy, self.attack_num)

    def froz_effect(self, enemy):
        print(f'{self.name}의 몸이 약간 녹은듯 하지만 공격엔 실패했다.\n')
        input()

    def battle_order(self, enemy, aattack):
        if aattack == 1:
            self.body_attack(enemy)
        elif aattack == 2:
            self.element_attack(enemy)
        elif aattack == 3:
            self.status_attack(enemy)
        input()

    def input_attack(self, enemy):
        print('-------------------------------------------------\n')
        print(f'| 내 {self.name}의 현재 체력 | {self.HP} / {self.max_hp} |')
        print(f'| 적 {enemy.name}의 현재 체력 | {enemy.HP} / {enemy.max_hp} |')
        if self.level >= 8:
            print(f'| 1 : 몸통 박치기 |   2 : {self.e_attack}   |  3 : {self.s_attack}  |')
            print(f'| 제한이 없습니다 | 남은 PP : {self.vapp} / {self.max_vapp} | 남은 PP : {self.sapp} / {self.max_sapp} |')
            self.attack_num = input('|공격을 선택하세요| ')
            if self.attack_num not in ['1', '2', '3']:
                while self.attack_num not in ['1', '2', '3']:
                    self.attack_num = input('|공격을 선택하세요| ')
        elif self.level >= 6:
            print(f'| 1 : 몸통 박치기 |   2 : {self.e_attack}   |')
            print(f'| 제한이 없습니다 | 남은 PP : {self.vapp} / {self.max_vapp} |')
            self.attack_num = input('|공격을 선택하세요| ')
            if self.attack_num not in ['1', '2']:
                while self.attack_num not in ['1', '2']:
                    self.attack_num = input('|공격을 선택하세요| ')
        else:
            print(f'| 1 : 몸통 박치기 |')
            print(f'| 제한이 없습니다 |')
            self.attack_num = input('|공격을 선택하세요| ')
            if self.attack_num not in ['1']:
                while self.attack_num not in ['1']:
                    self.attack_num = input('|공격을 선택하세요| ')
        self.attack_num = int(self.attack_num)
        print('\n-------------------------------------------------\n')
    
    def input_enemy_attack(self):
        if self.level >= 8:
            self.attack_num = random.choice([1, 2, 3])
        elif self.level >= 6:
            self.attack_num = random.choice([1, 2])
        else:
            self.attack_num = 1
    
    def status_inbattle(self, enemy):
        self.status_motion(enemy)
        if self.status == '마비':
            self.pal_effect(enemy)
        elif self.status == '동상':
            self.froz_effect(enemy)
        else:
            self.battle_order(enemy, self.attack_num)
    
    def battle(self, enemy):
        status = ['nomal', '마비', '동상', '화상', '흡수']
        print(f'\n앗! 야생의 {enemy.name}(lv.{enemy.level})을 만났다!!')
        input()

        while self.check_status() and enemy.check_status():
            self.input_attack(enemy)
            enemy.input_enemy_attack()
            if self.speed > enemy.speed:
                self.status_inbattle(enemy)
                if enemy.check_status() == False:
                    break   
                enemy.status_inbattle(self)
            elif self.speed == enemy.speed:
                order = random.choice([1, 2])
                if order == 1:
                    self.status_inbattle(enemy)
                    if enemy.check_status() == False:
                        break   
                    enemy.status_inbattle(self)
                else:
                    enemy.status_inbattle(self)
                    if self.check_status() == False:
                        break   
                    self.status_inbattle(enemy)
            else:
                enemy.status_inbattle(self)
                if self.check_status() == False:
                    break   
                self.status_inbattle(enemy)
        
        if self.check_status() == False:
            print('---------------------------------------')
            print(f'\n{self.name}는 더이상 싸울 힘이 없다.')
            input()
            print(f'{self.name}은 전투에서 지고 눈앞이 캄캄해 졌다.')
            input()
            print('---------------------------------------')

        else:
            print('---------------------------------------')
            print(f'\n{enemy.name}는 더이상 싸울 힘이 없다.')
            input()
            print(f'{self.name}이 전투에서 이기고 {enemy.level}의 경험치를 획득하였다!!')
            input()
            self.speed = self.heal_speed
            self.batttle_exp(enemy)
            if self.exp >= self.level:
                self.levelup()
                print(f'{self.name}의 레벨이 올라 {self.level}이 되었다.')
                input()
                if self.level % 3 == 0:
                    self.full_heal()
                else:
                    self.light_heal()
            print('---------------------------------------')
            

a = Pokemon('피카츄', 10, 'elec')
b = Pokemon('꼬북이', 10, 'water')
c = Pokemon('파이리', 10, 'fire')
d = Pokemon('이상해씨', 10, 'leef')

d.battle(b)

d.battle(c)

