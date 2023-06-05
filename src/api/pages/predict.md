<div class="container" style="margin-top: 67px;">
  <div class="card">
      <div class="card-header text-center">
          <h5><b>e-commerce prodect classification</b></h5>
      </div>
      <spam style="text-align: center">Pour prédire un pruit il suffit de télécharger l'image et puis le texte le décrivant.</spam>
      <div class="card-body">
          <div class="row">
              <div class="col-md-8">
                  <div class="card">
                      <div class="card-header text-center"><h5><b>Données</b></h5></div>
                      <form id="inputForm">
                      <div class="card-body">                            
                          <div class="row" id = "contenu">
                              <b> Insérer une image(jpeg, jpg, png)</b>
                              <form action="/uploadimages/" enctype="multipart/form-data" method="post">
                                  <input name="files" type="file" multiple>
                                  <input type="submit">
                              </form>  
                            </div>                         
                            <div class="row">
                              <b>Insérer une text(csv) </b>
                              <form action="/uploadtext/" enctype="multipart/form-data" method="post">
                                  <input name="files" type="file" multiple>
                                  <input type="submit">
                              </form>
                          </div>
                          <div class="card-footer text-center">
                              <button type = "button" onclick="getResult()" value = "submit" style="cursor: pointer;">Predict</button>
                          </div>
                      </div>
                  </form>
                  </div>
              </div>
              <div class="col-md-4">
                  <div class="card">
                  <div class="card-header text-center"><h5><b>Résultat : Classe prédite</b></h5></div>
                  <div class="card-body">
                      <div class="row">
                          <!-- Classe prédite->&nbsp;&nbsp; <span style="color:red"><p id="result"></p></span> -->
                          <span style="color:red"><p id="result"></p></span>
                      </div>
                      </div>
                  </div>
              </div>
          </div>
      </div>
  </div>
</div>
