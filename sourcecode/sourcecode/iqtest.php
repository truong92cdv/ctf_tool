<?php 

ob_start(); 
include('config.php');

?>

<style>
.button {
  display: inline-block;
  border-radius: 4px;
  background-color: #32CD32;
  border: none;
  color: #FFFFFF;
  text-align: center;
  font-size: 28px;
  padding: 10px;
  width: 150px;
  transition: all 0.5s;
  cursor: pointer;
  margin: 5px;
}

.button span {
  cursor: pointer;
  display: inline-block;
  position: relative;
  transition: 0.5s;
}

.button span:after {
  content: '\00bb';
  position: absolute;
  opacity: 0;
  top: 0;
  right: -20px;
  transition: 0.5s;
}

.button:hover span {
  padding-right: 25px;
}

.button:hover span:after {
  opacity: 1;
  right: 0;
}

.button1 {
    background-color: white; 
    color: black; 
    border: 2px solid #4CAF50;
}

input[type=text] {
    width: 20%;
    padding: 12px 20px;
    margin: 8px 0;
    box-sizing: border-box;
    border: 2px solid blue;
    border-radius: 4px;
}
</style>
<br>
<center><font size=10 color='red'>💮 💮 READY TO GET THE FLAG? 💮 💮</font></center>
<br>
<!-- ?is_debug=1 -->
<?php


function print_default()
{
unset($_COOKIE['saved']);
unset($_COOKIE['seed']);

if (isset($_POST["Command"]) && !empty($_POST["Command"]) && $_POST["Command"]==="start")
  {
    $saved = base64_encode("seed=".$GLOBALS['seed1']);
      setcookie("saved", $saved, time() + (86400 * 30), "/");
    setcookie("hash", md5($GLOBALS['secret'].$GLOBALS['seed1']), time() + (86400 * 30), "/");
    header("Refresh:0");
  }
else
  {
$str = <<<'EOD'
<br>
<form action="index.php" method="POST">
<input type="hidden" name="Command" value="start">
<center><button class="button" type="submit" style="vertical-align:middle"><span>Go </span></button></center>
</form>
EOD;
echo $str;
  }
}

function level1()
{
$question = <<<'EOD'
<center><font size=5 color='blue'>1. How many flowers are there? 👩🏼‍🎓</font></center><br>
<center>
🌻🌻🌻🌻
<form action="index.php" method="POST">
  <input type="checkbox" name="level1_choice" value="3"> 3<br>
  <input type="checkbox" name="level1_choice" value="2"> 2<br>
  <input type="checkbox" name="level1_choice" value="1"> 1<br>
  <input type="checkbox" name="level1_choice" value="4"> 4<br>
  <br>
  <button class="button button1" type="submit" style="vertical-align:middle"><span>submit </span></button>
</form>
</center>
EOD;
echo $question;

if (isset($_POST['level1_choice']) && !empty($_POST['level1_choice']))
  {  
    if($_POST['level1_choice']===$GLOBALS['answer1'])
    {
      $saved = base64_encode("seed=".$GLOBALS['seed2']);
      setcookie("saved", $saved, time() + (86400 * 30), "/");
      setcookie("hash", md5($GLOBALS['secret'].$GLOBALS['seed2']), time() + (86400 * 30), "/");
    }
    else
    {
      setcookie("saved", "", time() + (86400 * 30), "/");
      setcookie("hash", "", time() + (86400 * 30), "/");
    }
  header("Refresh:0");
  }
}


function level2()
{
$question = <<<'EOD'
<center><font size=5 color='blue'>2. Who is the singer of this song? 👨🏼‍🎓 </font></center><br>
<center>
<audio controls autoplay>
  <source src="assets/nhac.mp3" type="audio/mpeg">
</audio><p><p>
<form action="index.php" method="POST">
  <input type="checkbox" name="level2_choice" value="black"> Den Vau<br>
  <input type="checkbox" name="level2_choice" value="white"> Eminem <br>
  <input type="checkbox" name="level2_choice" value="pink"> Sep'ssss<br>
  <input type="checkbox" name="level2_choice" value="tsu"> tsug0d's <br>
  <br>
  <button class="button button1" type="submit" style="vertical-align:middle"><span>submit </span></button>
</form>
</center>
EOD;
echo $question;

if (isset($_POST['level2_choice']) && !empty($_POST['level2_choice']))
  {  
    if($_POST['level2_choice']===$GLOBALS['answer2'])
    {
      $saved = base64_encode("seed=".$GLOBALS['seed3']);
      setcookie("saved", $saved, time() + (86400 * 30), "/");
      setcookie("hash", md5($GLOBALS['secret'].$GLOBALS['seed3']), time() + (86400 * 30), "/");
    }
    else
    {
      setcookie("saved", "", time() + (86400 * 30), "/");
      setcookie("hash", "", time() + (86400 * 30), "/");
    }
  header("Refresh:0");
  }
}

function level3()
{
$question = <<<'EOD'
<center><font size=5 color='blue'>3. Which flower is this? 👨🏽‍🏫</font></center><br>
<center>
<img src="assets/tulip.jpg" /><br><br>
<form action="index.php" method="POST">
  <input type="text" name="level3_choice"><br>
  <br>
  <button class="button button1" type="submit" style="vertical-align:middle"><span>submit </span></button>
</form>
</center>
EOD;
echo $question;

if (isset($_POST['level3_choice']) && !empty($_POST['level3_choice']))
  {  
    if(strtolower($_POST['level3_choice'])===$GLOBALS['answer3'])
    {
      $saved = base64_encode("seed=".$GLOBALS['seed4']);
      setcookie("saved", $saved, time() + (86400 * 30), "/");
      setcookie("hash", md5($GLOBALS['secret'].$GLOBALS['seed4']), time() + (86400 * 30), "/");
    }
    else
    {
      setcookie("saved", "", time() + (86400 * 30), "/");
      setcookie("hash", "", time() + (86400 * 30), "/");
    }
  header("Refresh:0");
  }
}

function level4()
{
$question = <<<'EOD'
<center><font size=5 color='blue'>4. What animal is this? 🐘</font></center><br>
<center>
<img src="http://i.imgur.com/LFG0Fl3.jpg" /><br><br>
<form action="index.php" method="POST">
  <input type="text" name="level4_choice"><br>
  <br>
  <button class="button button1" type="submit" style="vertical-align:middle"><span>submit </span></button>
</form>
</center>
EOD;
echo $question;

if (isset($_POST['level4_choice']) && !empty($_POST['level4_choice']))
  {  
    if(strtolower($_POST['level4_choice'])===$GLOBALS['answer4'])
    {
      $saved = base64_encode("seed=".$GLOBALS['seed5']);
      setcookie("saved", $saved, time() + (86400 * 30), "/");
      setcookie("hash", md5($GLOBALS['secret'].$GLOBALS['seed5']), time() + (86400 * 30), "/");
    }
    else
    {
      setcookie("saved", "", time() + (86400 * 30), "/");
      setcookie("hash", "", time() + (86400 * 30), "/");
    }
  header("Refresh:0");
  }
}

function level5()
{
$question = <<<'EOD'
<center><font size=5 color='blue'>5. tsu handsome? [yes/no] 🕵🏻</font></center><br>
<center>
<br><br>
<form action="index.php" method="POST">
  <input type="text" name="level5_choice"><br>
  <br>
  <button class="button button1" type="submit" style="vertical-align:middle"><span>submit </span></button>
</form>
</center>
EOD;
echo $question;

if (isset($_POST['level5_choice']) && !empty($_POST['level5_choice']))
  {  
    if(strtolower($_POST['level5_choice'])===$GLOBALS['answer5'])
    {
      $saved = base64_encode("seed=".$GLOBALS['seed6']);
      setcookie("saved", $saved, time() + (86400 * 30), "/");
      setcookie("hash", md5($GLOBALS['secret'].$GLOBALS['seed6']), time() + (86400 * 30), "/");
    }
    else
    {
      setcookie("saved", "", time() + (86400 * 30), "/");
      setcookie("hash", "", time() + (86400 * 30), "/");
    }
  header("Refresh:0");
  }
}

function level6()
{
$question = <<<'EOD'
<center><font size=5 color='blue'>6. New Year Eve is on which day/month? 🌈</font></center><br>
<center>
<br><br>
<form action="index.php" method="POST">
  <input type="text" name="level6_choice"><br>
  <br>
  <button class="button button1" type="submit" style="vertical-align:middle"><span>submit </span></button>
</form>
</center>
EOD;
echo $question;

if (isset($_POST['level6_choice']) && !empty($_POST['level6_choice']))
  {  
    if(strtolower($_POST['level6_choice'])===$GLOBALS['answer6'])
    {
      $saved = base64_encode("seed=".$GLOBALS['seed7']);
      setcookie("saved", $saved, time() + (86400 * 30), "/");
      setcookie("hash", md5($GLOBALS['secret'].$GLOBALS['seed7']), time() + (86400 * 30), "/");
    }
    else
    {
      setcookie("saved", "", time() + (86400 * 30), "/");
      setcookie("hash", "", time() + (86400 * 30), "/");
    }
  header("Refresh:0");
  }
}

function level7()
{
$question = <<<'EOD'
<center><font size=5 color='blue'>7. 1 plus 2 equal 3, 2 plus 1 still equal 3, anh do em sao em chua do anh? 👼🏽</font></center><br>
<center>
<br><br>
<form action="index.php" method="POST">
  <input type="text" name="level7_choice"><br>
  <br>
  <button class="button button1" type="submit" style="vertical-align:middle"><span>submit </span></button>
</form>
</center>
EOD;
echo $question;

if (isset($_POST['level7_choice']) && !empty($_POST['level7_choice']))
  {  
    if(strtolower($_POST['level7_choice'])===$GLOBALS['answer7'])
    {
      $saved = base64_encode("seed=".$GLOBALS['seed8']);
      setcookie("saved", $saved, time() + (86400 * 30), "/");
      setcookie("hash", md5($GLOBALS['secret'].$GLOBALS['seed8']), time() + (86400 * 30), "/");
    }
    else
    {
      setcookie("saved", "", time() + (86400 * 30), "/");
      setcookie("hash", "", time() + (86400 * 30), "/");
    }
  header("Refresh:0");
  }
}

function level8()
{
$question = <<<'EOD'
<center><font size=5 color='blue'>8. If there are 6 apples and you take away 4, how many do you have? 🍎</font></center><br>
<center>
<br><br>
<form action="index.php" method="POST">
  <input type="text" name="level8_choice"><br>
  <br>
  <button class="button button1" type="submit" style="vertical-align:middle"><span>submit </span></button>
</form>
</center>
EOD;
echo $question;

if (isset($_POST['level8_choice']) && !empty($_POST['level8_choice']))
  {  
    if(strtolower($_POST['level8_choice'])===$GLOBALS['answer8'])
    {
      $saved = base64_encode("seed=".$GLOBALS['seed9']);
      setcookie("saved", $saved, time() + (86400 * 30), "/");
      setcookie("hash", md5($GLOBALS['secret'].$GLOBALS['seed9']), time() + (86400 * 30), "/");
    }
    else
    {
      setcookie("saved", "", time() + (86400 * 30), "/");
      setcookie("hash", "", time() + (86400 * 30), "/");
    }
  header("Refresh:0");
  }
}

function level9()
{
$question = <<<'EOD'
<center><font size=5 color='blue'>9. What goes up and down, but still remains in the same place? ↕️</font></center><br>
<center>
<br><br>
<form action="index.php" method="POST">
  <input type="text" name="level9_choice"><br>
  <br>
  <button class="button button1" type="submit" style="vertical-align:middle"><span>submit </span></button>
</form>
</center>
EOD;
echo $question;

if (isset($_POST['level9_choice']) && !empty($_POST['level9_choice']))
  {  
    if(strtolower($_POST['level9_choice'])===$GLOBALS['answer9'])
    {
      $saved = base64_encode("seed=".$GLOBALS['seed10']);
      setcookie("saved", $saved, time() + (86400 * 30), "/");
      setcookie("hash", md5($GLOBALS['secret'].$GLOBALS['seed10']), time() + (86400 * 30), "/");
    }
    else
    {
      setcookie("saved", "", time() + (86400 * 30), "/");
      setcookie("hash", "", time() + (86400 * 30), "/");
    }
  header("Refresh:0");
  }
}

function level10()
{
$question = <<<'EOD'
<center><font size=5 color='blue'>10. If there are 12 fish and half of them drown, how many are there? 🐟 🐡</font></center><br>
<center>
<br><br>
<form action="index.php" method="POST">
  <input type="text" name="level10_choice"><br>
  <br>
  <button class="button button1" type="submit" style="vertical-align:middle"><span>submit </span></button>
</form>
</center>
EOD;
echo $question;

if (isset($_POST['level10_choice']) && !empty($_POST['level10_choice']))
  {  
    if(strtolower($_POST['level10_choice'])===$GLOBALS['answer10'])
    {
      $saved = base64_encode("seed=".$GLOBALS['seed11']);
      setcookie("saved", $saved, time() + (86400 * 30), "/");
      setcookie("hash", md5($GLOBALS['secret'].$GLOBALS['seed11']), time() + (86400 * 30), "/");
    }
    else
    {
      setcookie("saved", "", time() + (86400 * 30), "/");
      setcookie("hash", "", time() + (86400 * 30), "/");
    }
  header("Refresh:0");
  }
}

function level11()
{
$question = <<<'EOD'
<center><font size=5 color='blue'>11. How much money that Bill Gate got? (You are so close to flag, keep answer hoho xD) 🏆</font></center><br>
<center>
<br><br>
<form action="index.php" method="POST">
  <input type="text" name="level11_choice"><br>
  <br>
  <button class="button button1" type="submit" style="vertical-align:middle"><span>submit </span></button>
</form>
</center>
EOD;
echo $question;

if (isset($_POST['level11_choice']) && !empty($_POST['level11_choice']))
  {  
    if(strtolower($_POST['level11_choice'])===$GLOBALS['answer11'])
    {
      $saved = base64_encode("seed=".$GLOBALS['seed12']);
      setcookie("saved", $saved, time() + (86400 * 30), "/");
      setcookie("hash", md5($GLOBALS['secret'].$GLOBALS['seed12']), time() + (86400 * 30), "/");
    }
    else
    {
      setcookie("saved", "", time() + (86400 * 30), "/");
      setcookie("hash", "", time() + (86400 * 30), "/");
    }
  header("Refresh:0");
  }
}

function level12()
{
$question = <<<'EOD'
<center><font size=5 color='blue'>12. This is a question! 😂</font></center><br>
<center>
<br><br>
<form action="index.php" method="POST">
  <input type="text" name="level12_choice"><br>
  <br>
  <button class="button button1" type="submit" style="vertical-align:middle"><span>submit </span></button>
</form>
</center>
EOD;
echo $question;

if (isset($_POST['level12_choice']) && !empty($_POST['level12_choice']))
  {  
    if(strtolower($_POST['level12_choice'])===$GLOBALS['answer12'])
    {
      $saved = base64_encode("seed=".$GLOBALS['seed13']);
      setcookie("saved", $saved, time() + (86400 * 30), "/");
      setcookie("hash", md5($GLOBALS['secret'].$GLOBALS['seed13']), time() + (86400 * 30), "/");
    }
    else
    {
      setcookie("saved", "", time() + (86400 * 30), "/");
      setcookie("hash", "", time() + (86400 * 30), "/");
    }
  header("Refresh:0");
  }
}

function level13()
{
$question = <<<'EOD'
<center><font size=5 color='blue'>13. Flower? 💖💖💖</font></center><br>
<center>
<br>
<form action="index.php" method="POST">
  <input type="checkbox" name="level13_choice" value="yes"> Of courses !!!!!<br>
  <input type="checkbox" name="level13_choice" value="yes"> Yes!!!! Yes!!!!!<br>
  <input type="checkbox" name="level13_choice" value="yes"> Absolutely Yes<br>
  <input type="checkbox" name="level13_choice" value="yes"> No Doubt!!!!!!<br>
  <br>
  <button class="button button1" type="submit" style="vertical-align:middle"><span>submit </span></button>
</form>
</center>
EOD;
echo $question;

if (isset($_POST['level13_choice']) && !empty($_POST['level13_choice']))
  {  
    if($_POST['level13_choice']===$GLOBALS['answer13'])
    {
      echo "<center><font size=10 color=blue>Okay...Good Game Well Play!</font><br><font size=5 color=green>".$GLOBALS['flag'];
      setcookie("saved", "", time() + (86400 * 30), "/");
      setcookie("hash", "", time() + (86400 * 30), "/");
    }
    else
    {
      setcookie("saved", "", time() + (86400 * 30), "/");
      setcookie("hash", "", time() + (86400 * 30), "/");
    }
  }
}
?>

<?php


$choice="";
if (isset($_COOKIE['saved']) && !empty($_COOKIE['saved']) && isset($_COOKIE['hash']) && !empty($_COOKIE['hash']))
{
  $saved = base64_decode($_COOKIE["saved"]);
  $seed = urldecode(substr($saved, 5 ));
}

if( md5($GLOBALS['secret'].$seed) === $_COOKIE['hash'] )
{    
  $level = $GLOBALS["seed_key"][$seed];
  if ($level === NULL)
  {
    $saved = "level=i&".$saved;
    $exp = explode("&", $saved);
    foreach($exp as $value)
    {
      parse_str($value);
    }
  }

    switch($level)
    {
      case ("i"):
        level1();
        break;
      case ("ii"):
        level2();
        break;
      case ("iii"):
        level3();
        break;
      case ("iv"):
        level4();
        break;
      case ("v"):
        level5();
        break;
      case ("vi"):
        level6();
        break;
      case ("vii"):
        level7();
        break;
      case ("viii"):
        level8();
        break;
      case ("ix"):
        level9();
        break;
      case ("x"):
        level10();
        break;
      case ("xi"):
        level11();
        break;
      case ("xii"):
        level12();
        break;
      case ("xiii"):
        level13();
        break;
      default:
        print_default();
    }
}
else
{
    print_default();
}

if(isset($_GET['is_debug']) && !empty($_GET['is_debug']) && $_GET['is_debug']==="1")
{
  show_source(__FILE__);
}

?>

<?php ob_flush(); ?>