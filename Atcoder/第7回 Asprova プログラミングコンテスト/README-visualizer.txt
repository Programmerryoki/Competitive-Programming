------------------------------------------
7th Asprova Programming Contest Visualizer
------------------------------------------

使い方
・visualizer.htmlをブラウザで開き、input fileに入力データファイルを、output fileに出力データファイルを指定するとガントチャートを表示します。大きいファイルだとやや時間がかかることがあります。Google Chrome, Firefoxなどではドラッグアンドドロップに対応しております。
・intervalではガントチャートに表示される時間の間隔を変更できます。読み込みに時間がかかる場合は大きな値を指定すると改善することがあります。
・各計画の上にマウスを乗せると開始/終了時刻などのポップアップが表示されます。
・表示色のトグルスイッチで、「入力した順」と「車種」、「停止原因」の色分類を切り替えられます。
・ガントチャート右上にあるボタンでガントチャートの拡大縮小ができます。
・ガントチャートは画面下のスクロールバーやShift+マウスホイール等で移動できます。
・ガントチャート上の作業を選択すると、その作業を含む一連の製造工程を示す線が描画されます。

使用上の注意
・このビジュアライザはすべてのブラウザで作動することを保証していません。推奨ブラウザはGoogle Chrome、動作ブラウザは Firefox、Microsoft Edgeです。
・このビジュアライザで計算された得点が、AtCoder上で計算される得点と一致することは保証されていません。大きな実数を扱った場合、有効桁数の問題で差異が出ることがあります。
・自分のプログラムの出力データの評価はoutput_checker.cppを使用し、ビジュアライザはあくまで出力データの視覚化のための補助的なツールとして使って頂けると幸いです。
・output_checker.cppとビジュアライザの評価結果が異なる場合はoutput_checker.cppの方を信用してください。
・特に、プログラムの出力データが制約を満たしていない場合は利益の横に WA と表示されます。このとき、数値、チャートはあくまでも参考値となります。

ライセンス
・© Asprova Corporation
・MIT License (URL: https://opensource.org/licenses/mit-license.php)
・longcontest visualizer framework を使って作成しています。(URL: https://github.com/kmyk/longcontest-visualizer-framework)
・デザインや初期のコードは rco-contest-2019 を参考にさせて頂きました。(URL: https://github.com/recruit-communications/rco-contest-2019)

------------------------------------------

HOW TO USE
・Open visualizer.html in a browser, and specify both input data file and output data file to display the Gantt chart. Large files may take some time. Google Chrome and Firefox support drag and drop.
・You can change the scale of the horizontal axis in the Gantt chart by specifying "interval". Please choose a large value if it takes time to load files.
・When you hover the mouse over a bar, information such as start/end time will be displayed on popup.
・By switching the color mode, you can change colors such that the same type of cars are displayed in the same color. You can also highlight works that caused stoppages.
・You can zoom in and out of the chart by clicking buttons on the top right of the chart.
・You can scroll the chart by dragging the scroll bars or Shift+wheel.
・When a bar on the Gantt chart is clicked, the connection lines are displayed. These lines connect adjacent works on the same car.

USAGE NOTES
・The visualizer is not guaranteed to work on all browsers. The recommended browser is Google Chrome. It also works on Mozilla FireFox and Microsoft Edge.
・The score calculated with this visualizer is not guaranteed to match the score calculated on AtCoder. When dealing with large real numbers, there may be differences due precision limitations.
・Use output_checker.cpp to evaluate the output data of your program. Consider visualizer as an auxiliary tool for visualizing the output data.
・If the evaluation results of output_checker.cpp and the visualizer are different, please trust output_checker.cpp.
・"WA" will be displayed next to the profits when the output data of the program does not meet the constraints. In this case, the numbers and charts are just only values for reference.

License agreement
・© Asprova Corporation
・MIT License (URL: https://opensource.org/licenses/mit-license.php)
・Created using the longcontest visualizer framework. URL: https://github.com/kmyk/longcontest-visualizer-framework)
・Design and initial code were taken from rco-contest-2019.(URL: https://github.com/recruit-communications/rco-contest-2019)
