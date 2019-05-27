#: /usr/bin

serverPort="10011"
imagedir="./project/resources/docImages/"
bookdir="./project/resources/"

echo "Have you placed all files into $bookdir properly?"
cd tools;
python3 lspdf.py $bookdir || echo " ! You must have  python3 in your  \$PATH and  allow it  to run in this program...  "
python3 lsimg.py $imagedir || echo " ! You are suggested to place some images into $imagedir as the pages of a default document ...  "

echo ;
echo "If successes, you can from your browser open  http://localhost:$serverPort"
python3 -m http.server $serverPort

