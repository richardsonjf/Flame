#!/bin/bash
echo "";	
cat << "EOF"
                                     )
                            )      ((     (
                           (        ))     )
                    )       )      //     (
               _   (        __    (     ~->>
        ,-----' |__,_~~___<'__`)-~__--__-~->> <
        | //  : | -__   ~__ o)____)),__ - '> >-  >
        | //  : |- \_ \ -\_\ -\ \ \ ~\_  \ ->> - ,  >>
        | //  : |_~_\ -\__\ \~'\ \ \, \__ . -<-  >>
        `-----._| `  -__`-- - ~~ -- ` --~> >
         _/___\_    //)_`//  | ||]
   _____[_______]_[~~-_ (.L_/  ||
  [____________________]' `\_,/'/
    ||| /          |||  ,___,'./
    ||| \          |||,'______|
    ||| /          /|| I==||
    ||| \       __/_||  __||__
-----||-/------`-._/||-o--o---o---
> \ /           Flame    :  A.I for Android Application Security
(_,-'`> .'      Authors  :  0xPwny - Haroon Awan / mrharoonawan@gmail.com
(_,'            Usage    :  flame jadx/apktool file.apk
EOF




Application=$2
Tool=$1

file_base=`basename $Application .apk`
dist_dir="Results/"$file_base""

if [ ! -f $Application ]; then
echo "[!]" $Application "not found !"
exit
fi

jadxx(){

if which jadx >/dev/null; then
true
else
echo "[!] You need to install JADX first ."
exit
fi


if [ -d "$dist_dir" ]; then
true
fi
$(mkdir -p $dist_dir)
echo "";
echo "[+] Decompiling in process "

jadx $Application -d $dist_dir > /dev/null
}


apkk(){

if which apktool >/dev/null; then
true
else
echo "[!] You need to install APKTOOL first ."
exit
fi
echo "";
echo "[+] Decompiling in process "
$(apktool d $Application -o $dist_dir -q)
}




if [ -z "$Tool" ];then
echo ""
exit

elif [ "$Tool" = "apktool" ];then
apkk

elif [ "$Tool" = "jadx" ];then
jadxx	
	else
echo "";
exit
fi

echo "[+] Application Successfully Decompiled "
python3 Flame.py $dist_dir $Tool
echo "[+] Extracting data at Results Folder"
echo "[+] Data Dumped Successful"
echo "[+] Checking Hidden Domains and Saving Results"
./AI_checker.sh
echo "";
echo "";
