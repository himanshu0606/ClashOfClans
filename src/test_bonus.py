import unittest
import king
import buildings as bd
import village
import points as pt


class TestAttackDamageofKing(unittest.TestCase):  # test if attack damage

    def setUp(self):
        self.V = village.createVillage(1)

    def test_Attack_Value_Negative(self):
        king_test = king.spawnKing((17, 35))
        self.assertGreater(king_test.attack, 0)

    def test_King_Change_Attr_Attack(self):
        king_test = king.spawnKing(pt.config['hero_pos'])
        init_speed = king_test.speed
        init_health = king_test.health
        init_max_health = king_test.max_health
        init_attack = king_test.attack
        init_AoE = king_test.AoE
        init_attack_radius = king_test.attack_radius
        init_alive = king_test.alive
        init_type = king_test.type
        hut = bd.Hut(pt.config['huts'][0], self.V)

        king_test.attack_target(hut, king_test.attack)

        self.assertEqual(init_speed, king_test.speed)
        self.assertEqual(init_health, king_test.health)
        self.assertEqual(init_max_health, king_test.max_health)
        self.assertEqual(init_attack, king_test.attack)
        self.assertEqual(init_AoE, king_test.AoE)
        self.assertEqual(init_attack_radius, king_test.attack_radius)
        self.assertEqual(init_alive, king_test.alive)
        self.assertEqual(init_type, king_test.type)

    def test_Attack_When_Dead(self):  # shouldnt attack when king is dead
        king_test = king.spawnKing((17, 35))
        king_test.alive = False
        hut = bd.Hut(pt.config['huts'][0], self.V)
        initial_health = hut.health
        king_test.attack_target(hut, king_test.attack)
        self.assertEqual(hut.health, initial_health)

        canon = bd.Cannon(pt.config['cannons'][0], self.V)
        initial_health = canon.health
        king_test.attack_target(canon, king_test.attack)
        self.assertEqual(canon.health, initial_health)

        wizard = bd.WizardTower(pt.config['wizard_towers'][0], self.V)
        initial_health = wizard.health
        king_test.attack_target(wizard, king_test.attack)
        self.assertEqual(wizard.health, initial_health)

        wall = bd.Wall(pt.config['walls_top'][0], self.V)
        initial_health = wall.health
        king_test.attack_target(wall, king_test.attack)
        self.assertEqual(wall.health, initial_health)

    # health of building should decrease on attack
    def test_Attack_Health_Deacrease_of_Building(self):
        king_test = king.spawnKing((17, 35))
        hut = bd.Hut(pt.config['huts'][0], self.V)
        initial_health = hut.health
        initial_attack = king_test.attack

        king_test.attack_target(hut, king_test.attack)
        self.assertGreater(initial_health, hut.health)
        self.assertEqual(hut.health, initial_health-initial_attack)
        self.assertEqual(initial_attack, king_test.attack)
        if king_test.attack < initial_health:
            self.assertFalse(hut.destroyed)
        else:
            self.assertLessEqual(hut.health, 0)
            self.assertTrue(hut.destroyed)

        canon = bd.Cannon(pt.config['cannons'][0], self.V)
        initial_health = canon.health
        king_test.attack_target(canon, king_test.attack)
        self.assertGreater(initial_health, canon.health)
        self.assertEqual(canon.health, initial_health-initial_attack)
        if king_test.attack < initial_health:
            self.assertFalse(canon.destroyed)
        else:
            self.assertLessEqual(canon.health, 0)
            self.assertTrue(canon.destroyed)

        wizard = bd.WizardTower(pt.config['wizard_towers'][0], self.V)
        initial_health = wizard.health
        king_test.attack_target(wizard, king_test.attack)
        self.assertGreater(initial_health, wizard.health)
        self.assertEqual(wizard.health, initial_health-initial_attack)
        if king_test.attack < initial_health:
            self.assertFalse(wizard.destroyed)
        else:
            self.assertLessEqual(wizard.health, 0)
            self.assertTrue(wizard.destroyed)

        wall = bd.Wall(pt.config['walls_top'][0], self.V)
        initial_health = wall.health
        king_test.attack_target(wall, king_test.attack)
        self.assertGreater(initial_health, wall.health)
        self.assertEqual(wall.health, initial_health-initial_attack)
        if king_test.attack < initial_health:
            self.assertFalse(wall.destroyed)
        else:
            self.assertLessEqual(wall.health, 0)
            self.assertTrue(wall.destroyed)

    # should destroy when building health zero
    def test_Attack_Destroy_When_Health_Zero(self):
        king_test = king.spawnKing((17, 35))
        hut = bd.Hut(pt.config['huts'][0], self.V)
        king_test.attack_target(hut, hut.max_health)
        self.assertLessEqual(hut.health, 0)
        self.assertTrue(hut.destroyed)

        canon = bd.Cannon(pt.config['cannons'][0], self.V)
        king_test.attack_target(canon, canon.max_health)
        self.assertLessEqual(canon.health, 0)
        self.assertTrue(canon.destroyed)

        wizard = bd.WizardTower(pt.config['wizard_towers'][0], self.V)
        king_test.attack_target(wizard, wizard.max_health)
        self.assertLessEqual(wizard.health, 0)
        self.assertTrue(wizard.destroyed)

        wall = bd.Wall(pt.config['walls_top'][0], self.V)
        king_test.attack_target(wall, wall.max_health)
        self.assertLessEqual(wall.health, 0)
        self.assertTrue(wall.destroyed)


if __name__ == '__main__':
    # Run the test suite and capture the output using TestResult
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAttackDamageofKing)
    result = unittest.TestResult()
    suite.run(result)
    f = open("output_bonus.txt", 'w')

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
