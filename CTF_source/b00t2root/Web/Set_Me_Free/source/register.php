<?php
include("connect.php");
include("sidebar.php");
?>
<h1>Register</h1>
<?php
if(isset($_POST['username'])){
    $name = $_POST['username'];
    $sql="select * from users where (username='$name');";
        $res=mysqli_query($conn,$sql);
        if (mysqli_num_rows($res) > 0) {
         echo "Username already exists";
        ?>
        <h2>User Not Registered</h2>
        <?php
        }
    else{
    $username = mysqli_real_escape_string($conn, $_POST['username']);
    $password = mysqli_real_escape_string($conn, $_POST['password']);
    $sql = "INSERT into users (username, password) values ('$username', '$password');";
    mysqli_query($conn, $sql);
    $sql = "INSERT into chck (userid, isRestricted) values ((select users.id from users where username='$username'), TRUE);";
    mysqli_query($conn, $sql);
    ?>
    <h2>SUCCESS!</h2>
    <?php
     }
} else {
?>
<legend>Account</legend>
<form action="register.php" method="post">
    <li>
        <label>Username</label>
        <input type="text" name="username">
    </li>
    <li>
        <label>Password</label>
        <input type="text" name="password">
    </li>
    <li>
        <input type="submit">
    </li>
</form>
<?php
}
highlight_file("register.php");
?>