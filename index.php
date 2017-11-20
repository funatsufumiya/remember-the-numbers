<?php

if(isset($_REQUEST['q'])){
  if(isset($_REQUEST['ignore']) && $_REQUEST['ignore'] != '0' ){
    $kana = $_REQUEST['q'];
    $output = exec("./scripts/kana2nums --ignore '$kana'");
  }else{
    $kana = $_REQUEST['q'];
    $output = exec("./scripts/kana2nums --strict '$kana'");
  }
}else{
  echo 'Usage: <a href="./?ignore=1&q=%E3%81%84%E3%81%A1%E3%81%94%E3%81%B1%E3%82%93%E3%81%A4%E3%81%A7%E3%82%88%E3%82%8D%E3%81%97%E3%81%8F">?q=いちごぱんつでよろしく&ignore=1</a>';
  exit();
}

?>
<!DOCTYPE html>
<html>
<head>
	<title>remember-the-numbers</title>

 	<script src="https://code.jquery.com/jquery-2.2.4.min.js"></script>
 	<script src="https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.8.3/underscore-min.js"></script>
	<link rel="stylesheet" href="https://unpkg.com/purecss@0.6.2/build/pure-min.css" integrity="sha384-UQiGfs9ICog+LwheBSRCt1o5cbyKIHbwjWscjemyBMT9YCUMZffs6UqUTd0hObXD" crossorigin="anonymous">
  <style>
  body {
    padding: 10px;
  }
  </style>
</head>
<body>
  '<?php echo $output; ?>'
</body>
</html>
