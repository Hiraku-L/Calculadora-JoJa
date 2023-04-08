let form = document.querySelector('#calculadora');

        function plantacao_pronta(data, dias) {
            return data + dias;
          }

        function dias_coleta(plantacao_pronta, producao) {
            plantacao_pronta = parseInt(plantacao_pronta);
            producao = parseInt(producao);
            let c = 0;
            let resultado = [plantacao_pronta];
            let producao_corrigida = producao - 1 + c;
            let dias = 28 - plantacao_pronta;
            let contador = 0;
            let quantas_producoes = Math.trunc(dias / producao_corrigida);
            for (c = 0; c < quantas_producoes; c++) {
              resultado.push(resultado[contador] + producao_corrigida);
              contador++;
            }
            return resultado;
          }

        function area(){
            let aspersor = parseInt(document.querySelector('#aspersor').value);
            let valorElemento = document.getElementById('quantidade').value;
            let quantidade = parseFloat(valorElemento);
            console.log(aspersor)
            console.log(quantidade)
                if (aspersor == 1) {
                    var area = 4*quantidade
                }
                else if (aspersor == 2) {
                    var area = 8*quantidade
                }
                if (aspersor == 3) {
                    var area = 24*quantidade
                }
                document.getElementById("area_result").innerHTML = "Área - Quantidade de sementes necessária: "+area
                //Valor das sementes
            let selectElement = document.querySelector('#semente');
            let valor;
            //pegar o valor do dia da plantação
            let dia_plantacao = parseInt(document.querySelector('#plantacao').value);
            let plantacao_pronta1;
            let dias_coleta1;
            dias_coleta1 = dias_coleta1;


            let sementes = parseInt(selectElement.value);
                if (sementes == 1){
                    valor = 40*area
                    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 8)
                    dias_coleta1 = "Coleta única"
                }
                else if (sementes == 2){
                    valor = 20*area
                    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 6)
                    dias_coleta1 = "Coleta única"
                }
                else if (sementes == 3){
                    valor = 40*area
                    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 4)
                    dias_coleta1 = "Coleta única"
                }
                else if (sementes == 4){
                    valor = 50*area
                    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 6)
                   dias_coleta1 = "Coleta única"
                }
                else if (sementes == 5){
                    valor = 20*area
                    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 4)
                    dias_coleta1 = "Coleta única"
                }
                else if (sementes == 6){
                    valor = 70*area
                    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 6)
                    dias_coleta1 = "Coleta única"
                }
                else if (sementes == 7){
                    valor = 80*area
                    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 12)
                    dias_coleta1 = "Coleta única"

                }
                else if (sementes == 8){
                    valor = 30*area
                    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 7)
                    dias_coleta1 = "Coleta única"
                }
                else if (sementes == 9){
                    valor = 100*area
                    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 8)
                   dias_coleta1 = dias_coleta(plantacao_pronta1, 4)
                }
                else if (sementes == 10){
                    valor = 100*area
                    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 13)
                    dias_coleta1 = "Coleta única"
                }
                else if (sementes == 11){
                    valor = 400*area
                    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 13)
                    dias_coleta1 = "Coleta única"
                }
                else if (sementes == 12){
                    valor = 200*area
                    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 8)
                    dias_coleta1 = "Coleta única"
                }
                else if (sementes == 13){
                    valor = 80*area
                    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 12)
                    dias_coleta1 = "Coleta única"
                }
                else if (sementes == 14){
                    valor = 50*area
                    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 8)
                    dias_coleta1 = "Coleta única"
                }
                else if (sementes == 15){
                    valor = 150*area
                    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 14)
                    dias_coleta1 = dias_coleta(plantacao_pronta1, 4)
                }
                else if (sementes == 16){
                    valor = 80*area
                    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 13)
                    dias_coleta1 = dias_coleta(plantacao_pronta1, 4)
                }
                else if (sementes == 17){
                    valor = 100*area
                    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 7)
                    dias_coleta1 = "Coleta única"
                }
                else if (sementes == 18){
                    valor = 40*area
                    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 7)
                    dias_coleta1 = dias_coleta(plantacao_pronta1, 3)
                }
                else if (sementes == 19){
                    valor = 40*area
                    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 6)
                    dias_coleta1 = "Coleta única"
                }
               else  if (sementes == 20){
                valor = 100*area
                plantacao_pronta1 = plantacao_pronta(dia_plantacao, 9)
                    dias_coleta1 = "Coleta única"
                }
                else if (sementes == 21){
                    valor = 50*area
                    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 11)
                   dias_coleta1 = dias_coleta(plantacao_pronta1, 4)
                }
                else if (sementes == 22){
                    valor = 10*area
                    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 4)
                    dias_coleta1 = "Coleta única"
                }
                else if (sementes == 23){
                    valor = 100*area
                    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 13)
                    dias_coleta1 = "Coleta única"
                }
                else if (sementes == 24){
                    valor = 30*area
                    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 8)
                    dias_coleta1 = "Coleta única"
                }
                else if (sementes == 25){
                    valor = 70*area
                    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 7)
                    dias_coleta1 = "Coleta única"
                }
                else if (sementes == 26){
                    valor = 20*area
                    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 5)
                    dias_coleta1 = dias_coleta(plantacao_pronta1, 5)
                }
                else if (sementes == 27){
                    valor = 20*area
                    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 6)
                    dias_coleta1 = "Coleta única"
                }
                else if (sementes == 28){
                    valor = 50*area
                    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 4)
                    dias_coleta1 = "Coleta única"
                }
                else if (sementes == 29){
                    valor = 200*area
                    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 12)
                    dias_coleta1 = "Coleta única"
                }
                else if (sementes == 30){
                    valor = 60*area
                    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 10)
                    dias_coleta1 = "Coleta única"
                }
                else if (sementes == 31){
                    valor = 240*area
                    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 7)
                    dias_coleta1 = dias_coleta(plantacao_pronta1, 5)
                }
            console.log(plantacao_pronta1)
            document.getElementById("custo_result").innerHTML = "Custo: "+ valor + "ouros"
            document.getElementById("dias_result").innerHTML = "Ficará pronto no dia: " + plantacao_pronta1
            if (dias_coleta1 == "Coleta única"){
                document.getElementById("plant_result").innerHTML = "Colheita única"
            }
            else{
                document.getElementById("plant_result").innerHTML = "Colheita nos dias: "+dias_coleta1
            }


        }


            
        
    // Imprime o resultado
    //document.getElementById("resultado").innerHTML = "O valor da plantação é R$" + valor.toFixed(2) + ", a plantação estará pronta para colheita em " + plantacao_pronta + " dias e haverá " + dias_coleta + " para a coleta das colheitas.";
    