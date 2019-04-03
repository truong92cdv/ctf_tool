<?php
include("connect.php");
include("sidebar.php");

include "flag.php";
?>
<h1>Login</h1>
<?php
if(isset($_POST['username'])){
    $username = mysqli_real_escape_string($conn, $_POST['username']);
    
    $sql = "SELECT * from users where username='$username';";
    $result = mysqli_query($conn, $sql);
    
    $row = $result->fetch_assoc();
    //var_dump($_POST);
    //var_dump($row);
    $res=mysqli_query($conn,$sql);
        if (mysqli_num_rows($res) === 0) {
         echo "Go register first";
        }
    

    elseif($_POST['username'] === $row['username'] and $_POST['password'] === $row['password']){
        ?>
        <h1>Logged in as <?php echo($username);?></h1>
        <?php

        $uid = $row['id'];
        $sql = "SELECT isRestricted from chck where userid='$uid' and isRestricted=TRUE;";
        $result = mysqli_query($conn, $sql);
        $row = $result->fetch_assoc();
        if($row['isRestricted']){
            ?>
            <h2>This is a restricted account</h2>

            <?php
        }else{
            ?>
            <h2><?php echo $flag;?></h2>
            <?php

        }


    ?>
    <h2>SUCCESS!</h2>
    <?php
    }
} else {
?>
<legend>Account</legend>
<form action="login.php" method="post">
    <ul>
        <li>
            <label>Username</label>
            <input type="text" name="username">
        </li>
        <li>
            <label>Password</label>
            <input type="text" name="password">
        </li>
        <li>
            <input type="submit" value="Login">
            </li>
    </ul>
</form>
<?php
}
highlight_file("login.php");
?>