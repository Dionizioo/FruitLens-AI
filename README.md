# FruitLens AI — Detector de Frutas e Rastreador Nutricional em Tempo Real

FruitLens AI é um projeto de visão computacional em tempo real que combina detecção de frutas utilizando Inteligência Artificial com análise nutricional e uma interface visual interativa.

O sistema utiliza um modelo YOLOv8 treinado para identificar frutas diretamente pela webcam, exibindo informações nutricionais como calorias e vitaminas em tempo real.

## Funcionalidades

* Detecção de frutas em tempo real com YOLOv8
* Dashboard nutricional interativo
* Estimativa de calorias por fruta detectada
* Filtro de estabilidade para reduzir falsos positivos
* Interface visual personalizada com OpenCV
* Monitoramento de FPS em tempo real
* Painel lateral dinâmico com informações nutricionais
* Suporte para gravação de vídeo

## Tecnologias Utilizadas

* Python
* YOLOv8 (Ultralytics)
* OpenCV
* NumPy
* Google Colab
* Deep Learning
* Visão Computacional

## Modelo de IA

O modelo de detecção foi treinado utilizando um dataset personalizado de frutas, com técnicas de data augmentation e fine tuning para melhorar a estabilidade e a precisão das detecções em tempo real.

## Melhorias Futuras

* Rastreamento de objetos com ByteTrack
* Sistema de estimativa de peso
* Dashboard web interativo
* Histórico nutricional
* Deploy para aplicações web e mobile

## Demonstração

Inferência em tempo real utilizando webcam com painel nutricional integrado.

<img src="https://github.com/Dionizioo/FruitLens-AI/blob/main/Exemplo.jpeg">
