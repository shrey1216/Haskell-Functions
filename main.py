import random
import unittest
class IPAddressConverter:
    
    def numToIpAddress(self,num):
        #convert into binary
        binary = format(num, "b")
        while(len(binary) < 32):
            binary = '0' + binary
        
        #now split them up into eights and calculate each part
        first = str(int(binary[0:8],2))
        second = str(int(binary[8:16],2))
        third = str(int(binary[16:24],2))
        fourth = str(int(binary[24:32],2))
        
        #return them concatenated as a string in IPv4 format 
        return first + '.' + second + '.' + third + '.' + fourth
        
        
    
    
    def ipAddressToNum(self,address):
        #(126 x 16777216) + (0 x 65536) + (0 x 256) + (1 x 1)
        temp = address.index('.')
        first = int(address[0:temp]) * 16777216
        address = address[(temp+1):len(address)]
        temp = address.index('.')
        second = int(address[0:temp]) * 65536
        address = address[(temp+1):len(address)]
        temp = address.index('.')
        third = int(address[0:temp]) * 256
        address = address[(temp+1):len(address)]
        fourth = int(address[0:len(address)])
        
        
        return first + second + third + fourth
        

class IPAddressConverterTest(unittest.TestCase):
    
    def test_ipAddressToNum(self):
        print('\n\nIP Address to Number Tests: \n')
        test = IPAddressConverter()
        
        #(actual,expected)
        try:
            self.assertEqual(test.ipAddressToNum('68.126.154.19'), 1149147667)
        except:
            print('Test 1 of conversion failed! Error with IP Address "68.126.154.19"')
        else:
            print('Successfully passed test 1 of converting an IP Address to a number')
        try:
            self.assertEqual(test.ipAddressToNum('26.94.94.197'), 442392261)
        except:
            print('Test 2 of conversion failed! Error with IP Address "26.94.94.197"')
        else:
            print('Successfully passed test 2 of converting an IP Address to a number')
        try:
            self.assertEqual(test.ipAddressToNum('2.202.192.53'), 46841909)
        except:
            print('Test 3 of conversion failed! Error with IP Address "2.202.192.53"')
        else:
            print('Successfully passed test 3 of converting an IP Address to a number')
        try:
            self.assertEqual(test.ipAddressToNum('157.52.103.108'), 2637457260)
        except:
            print('Test 4 of conversion failed! Error with IP Address "157.52.103.108"')
        else:
            print('Successfully passed test 4 of converting an IP Address to a number')
        try:
            self.assertEqual(test.ipAddressToNum('159.128.2.185'), 2675966649)
        except:
            print('Test 5 of conversion failed! Error with IP Address "159.128.2.185"')
        else:
            print('Successfully passed test 5 of converting an IP Address to a number')
        try:
            self.assertEqual(test.ipAddressToNum('80.93.150.109'), 1348310637)
        except:
            print('Test 6 of conversion failed! Error with IP Address "80.93.150.109"')
        else:
            print('Successfully passed test 6 of converting an IP Address to a number')
        try:
            self.assertEqual(test.ipAddressToNum('33.220.213.7'), 568120583)
        except:
            print('Test 7 of conversion failed! Error with IP Address "33.220.213.7"')
        else:
            print('Successfully passed test 7 of converting an IP Address to a number')
        try:
            self.assertEqual(test.ipAddressToNum('248.235.184.214'), 4176197846)
        except:
            print('Test 8 of conversion failed! Error with IP Address "248.235.184.214"')
        else:
            print('Successfully passed test 8 of converting an IP Address to a number')
        try:
            self.assertEqual(test.ipAddressToNum('240.94.136.0'), 4032727040)
        except:
            print('Test 9 of conversion failed! Error with IP Address "240.94.136.0"')
        else:
            print('Successfully passed test 9 of converting an IP Address to a number')
        try:
            self.assertEqual(test.ipAddressToNum('157.174.200.144'), 2645477520)
        except:
            print('Test 10 of conversion failed! Error with IP Address "157.174.200.144"')
        else:
            print('Successfully passed test 10 of converting an IP Address to a number')
    
    def test_numToIpAddress(self):
        print('\n\nNumber to IP Address Tests: \n')
        test = IPAddressConverter()
        
        #(actual,expected)
        try:
            self.assertEqual(test.numToIpAddress(1149147667),'68.126.154.19')
        except:
            print('Test 1 of conversion failed! Error with number "1149147667"')
        else:
            print('Successfully passed test 1 of converting a number to an IP Address')
        try:
            self.assertEqual(test.numToIpAddress(442392261),'26.94.94.197')
        except:
            print('Test 2 of conversion failed! Error with number "442392261"')
        else:
            print('Successfully passed test 2 of converting a number to an IP Address')
        try:
            self.assertEqual(test.numToIpAddress(46841909),'2.202.192.53')
        except:
            print('Test 3 of conversion failed! Error with number "46841909"')
        else:
            print('Successfully passed test 3 of converting a number to an IP Address')
        try:
            self.assertEqual(test.numToIpAddress(2637457260),'157.52.103.108')
        except:
            print('Test 4 of conversion failed! Error with number "2637457260"')
        else:
            print('Successfully passed test 4 of converting a number to an IP Address')
        try:
            self.assertEqual(test.numToIpAddress(2675966649),'159.128.2.185')
        except:
            print('Test 5 of conversion failed! Error with number "2675966649"')
        else:
            print('Successfully passed test 5 of converting a number to an IP Address')
        try:
            self.assertEqual(test.numToIpAddress(1348310637),'80.93.150.109')
        except:
            print('Test 6 of conversion failed! Error with number "1348310637"')
        else:
            print('Successfully passed test 6 of converting a number to an IP Address')
        try:
            self.assertEqual(test.numToIpAddress(568120583),'33.220.213.7')
        except:
            print('Test 7 of conversion failed! Error with number "568120583"')
        else:
            print('Successfully passed test 7 of converting a number to an IP Address')
        try:
            self.assertEqual(test.numToIpAddress(4176197846),'248.235.184.214')
        except:
            print('Test 8 of conversion failed! Error with number "4176197846"')
        else:
            print('Successfully passed test 8 of converting a number to an IP Address')
        try:
            self.assertEqual(test.numToIpAddress(4032727040),'240.94.136.0')
        except:
            print('Test 9 of conversion failed! Error with number "4032727040"')
        else:
            print('Successfully passed test 9 of converting a number to an IP Address')
        try:
            self.assertEqual(test.numToIpAddress(2645477520),'157.174.200.144')
        except:
            print('Test 10 of conversion failed! Error with number "2645477520"')
        else:
            print('Successfully passed test 10 of converting a number to an IP Address')
    

class MonoalphabeticCipher:
    def __init__ (self):
        self.key = None
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
    def generateKey(self): 
        
        #alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        keyTemp = ""

        while(len(keyTemp) < 26):
            letter = random.choice(self.alphabet)
            if letter not in keyTemp:
                keyTemp += letter
        
        
        self.key = keyTemp
        return self.key
        
    def encrypt(self, word):
        word = word.upper()
        encryptedWord = ""
        #alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for x in word:
            if(x == ' '):
                encryptedWord += ' '
            else:
                encryptedWord += self.key[self.alphabet.index(x)]
        return encryptedWord
        
        
    def decrypt(self, word):
        word = word.upper()
        decryptedWord = ""
        
        #alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for x in word:
            if(x == ' '):
                decryptedWord += ' '
            else:
                decryptedWord += self.alphabet[self.key.index(x)]
        return decryptedWord



class MonoalphabeticCipherTest(unittest.TestCase):
    def test_generateKey(self):
        print('\n\nGenerating Key Tests: \n')
        test1 = MonoalphabeticCipher()
        test2 = MonoalphabeticCipher()
        test3 = MonoalphabeticCipher()
        
        #(actual,expected)
        #see if the lengths of the generated keys are 26
        try:
            self.assertEqual(len(test1.generateKey()),26)
        except:
            print('Test 1 of generating a key failed! Inconsistency with the length of the key"')
        else:
            print('Successfully passed test 1 of generating a key')
        try:
            self.assertEqual(len(test2.generateKey()),26)
        except: 
            print('Test 2 of generating a key failed! Inconsistency with the length of the key"')
        else:
            print('Successfully passed test 2 of generating a key')
        try:
            self.assertEqual(len(test3.generateKey()),26)
        except: 
            print('Test 3 of generating a key failed! Inconsistency with the length of the key"')
        else: 
            print('Successfully passed test 3 of generating a key')
        #see if the generated keys contain each letter from the alphabet
        #see if each letter of the alphabet occurs in the generated key only once
        
        try:
            for x in test1.alphabet:
                self.assertTrue(x in test1.key)
                self.assertEqual(test1.key.count(x),1)
        except:
            print('Tests 4 and 5 of generating a key failed! Inconsistency with the values of the key"')
        else:
            print('Successfully passed tests 4 and 5 of generating a key')
        try:
            for x in test2.alphabet:
                self.assertTrue(x in test2.key)
                self.assertEqual(test2.key.count(x),1)
        except:
            print('Tests 6 and 7 of generating a key failed! Inconsistency with the values of the key"')
        else:
            print('Successfully passed tests 6 and 7 of generating a key')
        try:
            for x in test3.alphabet:
                self.assertTrue(x in test3.key)
                self.assertEqual(test3.key.count(x),1)
        except: 
            print('Tests 8 and 9 of generating a key failed! Inconsistency with the values of the key"')
        else: 
            print('Successfully passed tests 8 and 9 of generating a key')
            
        #Ensure that the same key isn't generated each time by comparing all three keys to each other
        #Each value should be false when compared
        try:
            self.assertFalse(test1.key == test2.key)
        except: 
            print('Test 10 of generating a key failed! A key might have been made more than once"')
        else: 
            print('Successfully passed test 10 of generating a key')
        try:
            self.assertFalse(test1.key == test3.key)
        except: 
            print('Test 11 of generating a key failed! A key might have been made more than once"')
        else: 
            print('Successfully passed test 11 of generating a key')
        try:
            self.assertFalse(test2.key == test3.key)
        except: 
            print('Test 12 of generating a key failed! A key might have been made more than once"')
        else: 
            print('Successfully passed test 12 of generating a key')
            
            
        
        
    def test_encrypt(self):
        print('\n\nEncryption Tests: ')

        test = MonoalphabeticCipher()
        
        #(actual,expected)
        #Using custom keys to test 
        #ABCDEFGHIJKLMNOPQRSTUVWXYZ    
        #XHDPZUMLQYGNAKIOFCSBEVTRWJ
        test.key = 'XHDPZUMLQYGNAKIOFCSBEVTRWJ\n'
        print('Key: ' + test.key)
        try:
            self.assertEqual(test.encrypt('Shreyan Wankavala'),'SLCZWXK TXKGXVXNX')
        except:
            print('Test 1 of encryption failed! Error with plaintext "Shreyan Wankavala"')
        else:
            print('Successfully passed test 1 of encryption')
        try:
            self.assertEqual(test.encrypt('He dreamed of leaving his law firm to open a portable dog wash'),'LZ PCZXAZP IU NZXVQKM LQS NXT UQCA BI IOZK X OICBXHNZ PIM TXSL')
        except:
            print('Test 2 of encryption failed! Error with plaintext "He dreamed of leaving his law firm to open a portable dog wash"')
        else:
            print('Successfully passed test 2 of encryption')
        try:
            self.assertEqual(test.encrypt('aaaaaaazzzzzzz'),'XXXXXXXJJJJJJJ')
        except:
            print('Test 3 of encryption failed! Error with plaintext "aaaaaaazzzzzzz"')
        else:
            print('Successfully passed test 3 of encryption')
        
        #ABCDEFGHIJKLMNOPQRSTUVWXYZ    
        #DCHMWREUSINLVXAJFPKOYTQGZB
        test.key = 'DCHMWREUSINLVXAJFPKOYTQGZB'
        print("\nNew Key: " + test.key + '\n')
        try:
            self.assertEqual(test.encrypt('Shreyan Wankavala'),'KUPWZDX QDXNDTDLD')
        except:
            print('Test 4 of encryption failed! Error with plaintext "Shreyan Wankavala"')
        else:
            print('Successfully passed test 4 of encryption')
        try:
            self.assertEqual(test.encrypt('After coating myself in vegetable oil I found my success rate skyrocketed'),'DROWP HADOSXE VZKWLR SX TWEWODCLW ASL S RAYXM VZ KYHHWKK PDOW KNZPAHNWOWM')
        except: 
            print('Test 5 of encryption failed! Error with plaintext "After coating myself in vegetable oil I found my success rate skyrocketed"')
        else:
            print('Successfully passed test 5 of encryption')
        try:
            self.assertEqual(test.encrypt('BBBBBYYYYY'),'CCCCCZZZZZ')
        except: 
            print('Test 6 of encryption failed! Error with plaintext "BBBBBYYYYY"')
        else:
            print('Successfully passed test 6 of encryption')
        
        
        #ABCDEFGHIJKLMNOPQRSTUVWXYZ    
        #KDFTQBZCMWUGOARXYHSVJILPNE
        test.key = 'KDFTQBZCMWUGOARXYHSVJILPNE'
        print("\nNew Key: " + test.key + '\n')
        try:
            self.assertEqual(test.encrypt('Sergio Giavanni Kitchens'),'SQHZMR ZMKIKAAM UMVFCQAS')
        except:
            print('Test 7 of encryption failed! Error with plaintext "Sergio Giavanni Kitchens"')
        else:
           print('Successfully passed test 7 of encryption') 
        try:
            self.assertEqual(test.encrypt('He felt that dining on the bridge brought romance to his relationship with his cat'),'CQ BQGV VCKV TMAMAZ RA VCQ DHMTZQ DHRJZCV HROKAFQ VR CMS HQGKVMRASCMX LMVC CMS FKV')
        except:
            print('Test 8 of encryption failed! Error with plaintext "He felt that dining on the bridge brought romance to his relationship with his cat"')
        else:
            print('Successfully passed test 8 of encryption')
        try:
            self.assertEqual(test.encrypt('AAAAAZZZZZ'),'KKKKKEEEEE')
        except: 
            print('Test 9 of encryption failed! Error with plaintext "AAAAAZZZZZ"')
        else:
            print('Successfully passed test 9 of encryption')
            
        
        #ABCDEFGHIJKLMNOPQRSTUVWXYZ
        #NVFJXWQTKLHGZPMDYEUABOCRSI
        test.key = 'NVFJXWQTKLHGZPMDYEUABOCRSI'
        print("\nNew Key: " + test.key + '\n')
        try:
            self.assertEqual(test.encrypt('ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'NVFJXWQTKLHGZPMDYEUABOCRSI')
        except: 
            print('Test 10 of encryption failed! Error with plaintext "ABCDEFGHIJKLMNOPQRSTUVWXYZ"')
        else: 
            print('Successfully passed test 10 of encryption\n')
        
        
    
    
    def test_decrypt(self):
        print('\n\nDecryption Tests: ')
        test = MonoalphabeticCipher()
        print('Key: ' + test.generateKey())
        
        
        #(actual,expected)
        #The actual value is the decryption of the encryption
        #The expected value is the upper case message put in for encryption
        try:
            self.assertEqual(test.decrypt(test.encrypt('The changing of down comforters to cotton bedspreads always meant the squirrels had returned')),'THE CHANGING OF DOWN COMFORTERS TO COTTON BEDSPREADS ALWAYS MEANT THE SQUIRRELS HAD RETURNED')
        except:
            print('Test 1 of decryption failed! Error with plaintext "he changing of down comforters to cotton bedspreads always meant the squirrels had returned"')
        else:
            print('\nSuccessfully passed test 1 of decryption')
        try:
            self.assertEqual(test.decrypt(test.encrypt('Stimulation')),'STIMULATION')
        except:
            print('Test 2 of decryption failed! Error with plaintext "Stimulation"')
        else:
            print('Successfully passed test 2 of decryption')
        try:
            self.assertEqual(test.decrypt(test.encrypt('Poison ivy grew through the fence they said was impenetrable')),'POISON IVY GREW THROUGH THE FENCE THEY SAID WAS IMPENETRABLE')
        except:
            print('Test 3 of decryption failed! Error with plaintext "Poison ivy grew through the fence they said was impenetrable"')
        else:
            print('Successfully passed test 3 of decryption')
        try:
            self.assertEqual(test.decrypt(test.encrypt('YEEZY YEEZY YEEZY JUST JUMPED OVER JUMPMAN')),'YEEZY YEEZY YEEZY JUST JUMPED OVER JUMPMAN')
        except:
            print('Test 4 of decryption failed! Error with plaintext "YEEZY YEEZY YEEZY JUST JUMPED OVER JUMPMAN"')
        else:
            print('Successfully passed test 4 of decryption')
        try:
            self.assertEqual(test.decrypt(test.encrypt('She can live her life however she wants as long as she listens to what I have to say')),'SHE CAN LIVE HER LIFE HOWEVER SHE WANTS AS LONG AS SHE LISTENS TO WHAT I HAVE TO SAY')
        except:
            print('Test 5 of decryption failed! Error with plaintext "She can live her life however she wants as long as she listens to what I have to say"')
        else:
            print('Successfully passed test 5 of decryption')
        
        #New key
        test.generateKey()
        print('\nNew Key: ' + test.generateKey() + '\n')
        try:
            self.assertEqual(test.decrypt(test.encrypt('Clock')),'CLOCK')
        except:
            print('Test 6 of decryption failed! Error with plaintext "Clock"')
        else:
            print('Successfully passed test 6 of decryption')
        try:
            self.assertEqual(test.decrypt(test.encrypt('Memorial')),'MEMORIAL')
        except:
            print('Test 7 of decryption failed! Error with plaintext "Memorial"')
        else:
            print('Successfully passed test 7 of decryption')
        try:
            self.assertEqual(test.decrypt(test.encrypt('Just go ahead and press that button')),'JUST GO AHEAD AND PRESS THAT BUTTON')
        except:
            print('Test 8 of decryption failed! Error with plaintext "Just go ahead and press that button"')
        else:
            print('Successfully passed test 8 of decryption')
        try:
            self.assertEqual(test.decrypt(test.encrypt('Promise')),'PROMISE')
        except:
            print('Test 9 of decryption failed! Error with plaintext "Promise"')
        else:
            print('Successfully passed test 9 of decryption')
        try:
            self.assertEqual(test.decrypt(test.encrypt('Competition')),'COMPETITION')
        except:
            print('Test 10 of decryption failed! Error with plaintext "Competition"')
        else:
            print("Successfully passed test 10 of decryption")


if __name__ == '__main__':
    unittest.main()
    
    
    
    
    


    

