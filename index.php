<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">

    <link href="main.css" rel="stylesheet" type="text/css">

    <title>Siren</title>
  </head>
  <body>

    <nav class="navbar navbar-light bg-light fixed-top navbar-expand-sm">
            <!-- <div class="container-fluid"> -->
            <a class="navbar-brand" href="#">Siren</a>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav mr-auto">
                    <li class="nav-item active"><a class="nav-link" href="http://35.226.240.223/index.php">Home</a></li>
                    <li class="nav-item"><a class="nav-link" href="http://35.226.240.223/about.html">About</a></li>
                    <li class="nav-item"><a class="nav-link" href="https://github.com/vfranco2/Siren">The Werk</a></li>
                </ul>
            </div>
        </nav>

        <div class="container">
            <div class="cont1">
		<div class="row text-center justify-content-center">
			<div class="col">
               			<h2>Siren</h2>
				<form method="post" action="">
                			<input class="form-control" type="text" placeholder="Paste a Genius Lyric URL here" aria-label="Search" name="searchlyr"/>
				</form>
			</div>
		</div>
            </div>
	    <div class="container">
		<div class="row text-center">
			<div class="col">
				<h4>Original</h4>
				<?php
                                        if( isset($_POST['searchlyr']) ) {
                                                $url = $_POST['searchlyr'];
						$orig = substr(shell_exec("python3 scr.py " . $url . " 2>&1"),2,-2);
						echo $orig;
                                        }
                                ?>
			</div>
			<div class="col">
                                <h4>Improved</h4>
				<?php
                                        if( isset($_POST['searchlyr']) ) {
                                                $url = $_POST['searchlyr'];
                                                $impr = substr(shell_exec("python3 lyr.py " . $url . " 2>&1"),2,-2);
						echo $impr;
                                        }
                                ?>
                        </div>
		</div>
	    </div>
      </div>
  </body>
</html>
