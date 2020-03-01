<html lang="en">
   <head>
      <meta charset="utf-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
      <link href="resources/main.css" rel="stylesheet" type="text/css">
      <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
      <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
      <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
      <title>Siren</title>
   </head>
   <body>
      <?php include("resources/head.html") ?>
      <br><br>
      <div class="container">
         <div class="row text-center justify-content-center">
            <div class="col">
               <h2>Siren</h2>
               <h4>Search an artist or song.</h4>
               <form autocomplete="off" method="post" action="">
                   <input id="genlink" class="form-control black-border" type="text" placeholder="Search" aria-label="Search" name="searchlyr"/>
                   <div class="mypanel"></div>
               </form>

               <script>
               $(function () {
                 var getData = function (request, response) {
                   var url = 'https://api.genius.com/search?access_token=84WMdKzbMh7QnirAdTu5nj8iw0zkQ9vKVcAJHJdZ_miCxwgaplV_oogM-rlKRpXN&q=' + request.term;
                     $.getJSON(url,function (data) {
                             var data = [`${data.response.hits[0].result.full_title} | ${data.response.hits[0].result.url}`,
                                         `${data.response.hits[1].result.full_title} | ${data.response.hits[1].result.url}`,
                                         `${data.response.hits[2].result.full_title} | ${data.response.hits[2].result.url}`,
                                         `${data.response.hits[3].result.full_title} | ${data.response.hits[3].result.url}`,
                                         `${data.response.hits[4].result.full_title} | ${data.response.hits[4].result.url}`]
                             response(data);
                         });
                 };

                 var selectItem = function (event, ui) {
                     $("#genlink").val(ui.item.value);
                     return false;
                 }

                 $("#genlink").autocomplete({
                     source: getData,
                     select: selectItem,
                     minLength: 4,
                     change: function() {
                         $("#genlink").val("").css("display", 2);
                     }
                 });
              });
              </script>

            </div>
         </div>
         <div class="container">
            <div class="row text-center">
               <div class="col">
                  <h4>Original</h4>
                  <div style="color:#000000">
                     <?php
                        if( isset($_POST['searchlyr']) ) {
                          $url = $_POST['searchlyr'];
                          $send = trim(substr($url, strpos($url, '|') + 1));
                          $scraped = substr(shell_exec("python3 py/scr.py " . $send . " 2>&1"),2,-2);
                          echo str_replace('@', "'", $scraped);
                        }
                        ?>
                  </div>
               </div>
               <div class="col">
                  <h4>Improved</h4>
                  <div style="color:#000000">
                     <?php
                        if( isset($_POST['searchlyr']) ) {
                          $url = $_POST['searchlyr'];
                          $send = trim(substr($url, strpos($url, '|') + 1));
                          $impr = substr(shell_exec("python3 py/lyr.py " . $send . " 2>&1"),2,-2);
                          echo str_replace('@', "'", $impr);
                        }
                        ?>
                  </div>
               </div>
            </div>
         </div>
      </div>
   </body>
</html>
