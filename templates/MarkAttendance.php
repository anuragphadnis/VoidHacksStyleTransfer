<?php
  session_start();
  require_once("pdo.php");
  $now = new DateTime();
  $now->format('Y-m-d H:i:s');

  if(isset($_GET['id']))
  {
    // ADD TO Attendance table
    $data = $pdo->prepare("INSERT INTO Attendance
    (member_id,working_date)
    VALUES(
        :member_id,
        :date_id
    )");
    $data->execute(array(":member_id"=>$_GET['id'],":date_id"=>$now->format('Y-m-d H:i:s')));
    header("Location:MarkAttendance.php");
  }
  $read=$pdo->prepare("SELECT * FROM Lead WHERE head_id = :id");
  $read->execute(array(":id"=>$_SESSION['id']));

?>
<html>
<head>
    <title>Worst Hackathon</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width = device-width, initial-scale = 1">

    <link rel="stylesheet" type="text/css" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" >
    <link rel="stylesheet" type="text/css" href="style5.css">
    <style>
        .input-group-addon {
        min-width:150px;
        text-align:left;
    }
    </style>
</head>
<body>
    <div class="wrapper">
    <?php if (isset($_SESSION['id'])&&$_SESSION['role']=='0') include "navbar.php";
                else if(isset($_SESSION['id'])&&$_SESSION['role']=='1')  include "navbar_user.php";
                else include "navbar_user.php";?>
      <div class="container-fluid row" id="content">
        <div class="page-header">
          <table class="table table-striped">
          <thead>
            <tr>
              <th>Name</th>
              <th>Contact Number</th>
              <th>Mark Attendance</th>
            </tr>
          </thead>
          <tbody>
            <?php
            while($data = $read->fetch(PDO::FETCH_ASSOC))
            {
              $data_member=$pdo->prepare("SELECT * FROM Members WHERE member_id = :id");
              $data_member->execute(array(":id"=>$data['member_id']));
              $data_member = $data_member->fetch(PDO::FETCH_ASSOC);
                echo"
              <tr>
                <td>".$data_member['name']."</td>
                <td>".$data_member['ph']."</td>
                <td><a class='link-black' href='MarkAttendance.php?id=".$data['member_id']."'>Mark Attendance</a></td>
              </tr>";

            }
            ?>
          </tbody>
        </table>
      </div>
    </div>
    </div>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
    <script type="text/javascript" src="script.js"></script>
</body>
</html>
