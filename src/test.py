import unittest
import king
import buildings as bd
import village
import points as pt

class TestMoveKing(unittest.TestCase):
    def setUp(self):
        self.V= village.createVillage(1)
    
    def test_King_Speed(self):
        king_test=king.spawnKing(pt.config['hero_pos'])
        self.assertGreater(king_test.speed,0)
    
    def test_King_Change_Attr_Up(self):
        king_test=king.spawnKing(pt.config['hero_pos'])
        init_speed=king_test.speed
        init_health=king_test.health
        init_max_health=king_test.max_health
        init_attack=king_test.attack
        init_AoE=king_test.AoE
        init_attack_radius=king_test.attack_radius
        init_alive=king_test.alive
        init_type=king_test.type

        king_test.move("up",self.V)

        self.assertEqual(init_speed,king_test.speed)
        self.assertEqual(init_health,king_test.health)
        self.assertEqual(init_max_health,king_test.max_health)
        self.assertEqual(init_attack,king_test.attack)
        self.assertEqual(init_AoE,king_test.AoE)
        self.assertEqual(init_attack_radius,king_test.attack_radius)
        self.assertEqual(init_alive,king_test.alive)
        self.assertEqual(init_type,king_test.type)
    
    def test_King_Change_Attr_Down(self):
        king_test=king.spawnKing(pt.config['hero_pos'])
        init_speed=king_test.speed
        init_health=king_test.health
        init_max_health=king_test.max_health
        init_attack=king_test.attack
        init_AoE=king_test.AoE
        init_attack_radius=king_test.attack_radius
        init_alive=king_test.alive
        init_type=king_test.type

        king_test.move("down",self.V)

        self.assertEqual(init_speed,king_test.speed)
        self.assertEqual(init_health,king_test.health)
        self.assertEqual(init_max_health,king_test.max_health)
        self.assertEqual(init_attack,king_test.attack)
        self.assertEqual(init_AoE,king_test.AoE)
        self.assertEqual(init_attack_radius,king_test.attack_radius)
        self.assertEqual(init_alive,king_test.alive)
        self.assertEqual(init_type,king_test.type)
    
    def test_King_Change_Attr_Left(self):
        king_test=king.spawnKing(pt.config['hero_pos'])
        init_speed=king_test.speed
        init_health=king_test.health
        init_max_health=king_test.max_health
        init_attack=king_test.attack
        init_AoE=king_test.AoE
        init_attack_radius=king_test.attack_radius
        init_alive=king_test.alive
        init_type=king_test.type

        king_test.move("left",self.V)

        self.assertEqual(init_speed,king_test.speed)
        self.assertEqual(init_health,king_test.health)
        self.assertEqual(init_max_health,king_test.max_health)
        self.assertEqual(init_attack,king_test.attack)
        self.assertEqual(init_AoE,king_test.AoE)
        self.assertEqual(init_attack_radius,king_test.attack_radius)
        self.assertEqual(init_alive,king_test.alive)
        self.assertEqual(init_type,king_test.type)
    
    def test_King_Change_Attr_Right(self):
        king_test=king.spawnKing(pt.config['hero_pos'])
        init_speed=king_test.speed
        init_health=king_test.health
        init_max_health=king_test.max_health
        init_attack=king_test.attack
        init_AoE=king_test.AoE
        init_attack_radius=king_test.attack_radius
        init_alive=king_test.alive
        init_type=king_test.type

        king_test.move("right",self.V)

        self.assertEqual(init_speed,king_test.speed)
        self.assertEqual(init_health,king_test.health)
        self.assertEqual(init_max_health,king_test.max_health)
        self.assertEqual(init_attack,king_test.attack)
        self.assertEqual(init_AoE,king_test.AoE)
        self.assertEqual(init_attack_radius,king_test.attack_radius)
        self.assertEqual(init_alive,king_test.alive)
        self.assertEqual(init_type,king_test.type)


    def test_King_Move_IfDead(self):
        king_test=king.spawnKing(pt.config['hero_pos'])
        king_test.alive=False
        pos= [king_test.position[0],king_test.position[1]]

        king_test.move("up",self.V)
        self.assertEqual(pos,king_test.position)

        king_test.move("down",self.V)
        self.assertEqual(pos,king_test.position)
        king_test.move("left",self.V)
        self.assertEqual(pos,king_test.position)
        king_test.move("rigth",self.V)
        self.assertEqual(pos,king_test.position)
    

    
    def test_King_Move_Up(self): # test up movement of king
        dim= pt.config['dimensions']
        dim_c=dim[1]
        dim_r=dim[0]

        for i in range(dim_r):
            for j in range(dim_c):
                vmap=self.V.map
                if(vmap[i][j] != pt.BLANK and vmap[i][j] != pt.SPAWN):
                    continue
                king_test= king.spawnKing((i,j))
                org_r=king_test.position[0]
                org_c=king_test.position[1]
                initial_speed=king_test.speed

                king_test.move('up',self.V)
                self.assertEqual(initial_speed,king_test.speed) # speed shouldn't change
                self.assertEqual(king_test.facing,'up')
                self.assertEqual(org_c,king_test.position[1]) # column shouldnt change
                self.assertGreaterEqual(king_test.position[0],0) # row should be greater than 0
                self.assertLess(king_test.position[0],dim_r) # row should be less than maximum rows
                self.assertGreaterEqual(org_r,king_test.position[0]) # row should decrease or be same
                self.assertEqual(pt.HERO_POS,king_test.position)
                
                for k in range(king_test.speed):
                    org_r-=1
                    if (org_r<0):
                        org_r+=1
                        break
                    elif(vmap[org_r][j]!=pt.BLANK and vmap[org_r][j] != pt.SPAWN):
                        org_r+=1
                        break
                self.assertEqual(king_test.position[0],org_r)
    
    def test_King_Move_Down(self): # test down movement of king
        dim= pt.config['dimensions']
        dim_c=dim[1]
        dim_r=dim[0]

        for i in range(dim_r):
            for j in range(dim_c):
                vmap=self.V.map
                if(vmap[i][j] != pt.BLANK and vmap[i][j] != pt.SPAWN):
                    continue
                king_test= king.spawnKing((i,j))
                org_r=king_test.position[0]
                org_c=king_test.position[1]
                initial_speed=king_test.speed

                king_test.move('down',self.V)
                self.assertEqual(initial_speed,king_test.speed) # speed shouldn't change
                self.assertEqual(king_test.facing,'down') # should be facing down
                self.assertEqual(org_c,king_test.position[1]) # column shouldnt change
                self.assertGreaterEqual(king_test.position[0],0) # row should be greater than equal to 0
                self.assertLess(king_test.position[0],dim_r) # row should be less than maximum rows
                self.assertGreaterEqual(king_test.position[0],org_r) # row should increase or be same
                self.assertEqual(pt.HERO_POS,king_test.position)
                for k in range(king_test.speed):
                    org_r+=1
                    if(org_r>=dim_r):
                        org_r-=1
                        break
                    elif(vmap[org_r][j]!=pt.BLANK and vmap[org_r][j] != pt.SPAWN):
                        org_r-=1
                        break
                self.assertEqual(king_test.position[0],org_r)

    def test_King_Move_Left(self): # test left movement of king
        dim= pt.config['dimensions']
        dim_c=dim[1]
        dim_r=dim[0]

        for i in range(dim_r):
            for j in range(dim_c):
                vmap=self.V.map
                if(vmap[i][j] != pt.BLANK and vmap[i][j] != pt.SPAWN):
                    continue
                king_test= king.spawnKing((i,j))
                org_r=king_test.position[0]
                org_c=king_test.position[1]
                initial_speed=king_test.speed

                king_test.move('left',self.V)
                self.assertEqual(initial_speed,king_test.speed) # speed shouldn't change
                self.assertEqual(king_test.facing,'left') # should be facing left
                self.assertEqual(org_r,king_test.position[0]) # row shouldnt change
                self.assertGreaterEqual(king_test.position[1],0) # column should be greater than 0
                self.assertLess(king_test.position[1],dim_c) # column should be less than dim_c
                self.assertGreaterEqual(org_c,king_test.position[1]) # column should decrease or be same
                self.assertEqual(pt.HERO_POS,king_test.position)
                for k in range(king_test.speed):
                    org_c-=1
                    if(org_c<0):
                        org_c+=1
                        break
                    elif(vmap[i][org_c]!=pt.BLANK and vmap[i][org_c] != pt.SPAWN):
                        org_c+=1
                        break
                self.assertEqual(org_c,king_test.position[1])
    
    def test_King_Move_Right(self): # test right movement of king
        dim= pt.config['dimensions']
        dim_c=dim[1]
        dim_r=dim[0]

        for i in range(dim_r):
            for j in range(dim_c):
                vmap=self.V.map
                if(vmap[i][j] != pt.BLANK and vmap[i][j] != pt.SPAWN):
                    continue
                king_test= king.spawnKing((i,j))
                org_r=king_test.position[0]
                org_c=king_test.position[1]
                initial_speed=king_test.speed

                king_test.move('right',self.V)
                self.assertEqual(initial_speed,king_test.speed) # speed shouldn't change
                self.assertEqual(king_test.facing,'right') # should be facing right
                self.assertEqual(org_r,king_test.position[0]) # shoulnt change row
                self.assertGreaterEqual(king_test.position[1],0) # column should be greater or equal to 0
                self.assertLess(king_test.position[1],dim_c) # column should be less than dim_c
                self.assertGreaterEqual(king_test.position[1],org_c) # column should decrease or be same
                self.assertEqual(pt.HERO_POS,king_test.position)

                for k in range(king_test.speed):
                    org_c+=1
                    if(org_c>=dim_c):
                        org_c-=1
                        break
                    elif(vmap[i][org_c]!=pt.BLANK and vmap[i][org_c] != pt.SPAWN):
                        org_c-=1
                        break
                self.assertEqual(org_c,king_test.position[1])
        


if __name__ == '__main__':
    # Run the test suite and capture the output using TestResult
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMoveKing)
    result = unittest.TestResult()
    suite.run(result)
    f= open("output.txt",'w')

    # Check if all tests passed and print True or False accordingly
    if result.wasSuccessful():
        f.write("True")
        f.close()
        # print("True")
        exit(0)
    else:
        f.write("False")
        # print("False")
        f.close()
        exit(1)

# unittest.main()
