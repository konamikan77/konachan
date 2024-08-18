/*  これはこなちゃんbot2222222222のプログラム  */
const http = require('http');
const querystring = require('querystring');
const Intents = require("discord.js");
const discord = require('discord.js');
const client = new discord.Client({ intents: [discord.Intents.FLAGS.GUILDS, discord.Intents.FLAGS.GUILD_MESSAGES] });
//require('dotenv').config();
//const { Client, Intents} = require('discord.js');

http.createServer(function(req, res){
 if (req.method == 'POST'){
   var data = "";
   req.on('data', function(chunk){
     data += chunk;
   });
   req.on('end', function(){
     if(!data){
        console.log("No post data");
        res.end();
        return;
     }
     var dataObject = querystring.parse(data);
     console.log("post:" + dataObject.type);
     if(dataObject.type == "wake"){
       console.log("Woke up in post");
       res.end();
       return;
     }
     res.end();
   });
 }
 else if (req.method == 'GET'){
   res.writeHead(200, {'Content-Type': 'text/plain'});
   res.end('Discord Bot is active now\n');
 }
}).listen(3000);

client.on('ready', message =>{
 console.log('Bot準備完了～');
 client.user.setPresence({ activity: { name: 'げーむ' } });
});

//ファイル書き出しプログラム作成中
var SETTING_DIR = "./public/export/"
var SETTING_FILE = "./public/export/{}.js"
var SETTINGS = "./public/export/*"
var Room_Status = "OFF"
var Room_Number = ""
var Room_ID = ""
var Reminder_Status = "OFF"
var Reminder_ID = ""
var Reminder_Message = "たいてね"

function init() {
  Room_Status = "OFF"
  Room_Number = ""
  Room_ID = ""
  Reminder_Status = "OFF"
  Reminder_ID = ""
  Reminder_Message = "たいてね"
}

//ここから本文
client.on('ready', async () => {
  console.log('おねね');
  const LOchannel = client.channels.cache.get('955296240533372989'); //聞き専チャンネルのID  Listen Only channel
  const RoomNumberChannel = client.channels.cache.get('975141931610951690')// ここは部屋番号チャンネルIDを記入

  // 〇〇分にシフト交代・リマインド等  ----------  [ bot動かすときはここを入力 ]  ----------------↓

  var cron = require('node-cron');
  cron.schedule('5 * * * *', () => {
    LOchannel.send('たいてね')
  });

  var cron = require('node-cron');
  cron.schedule('18 * * * *', () => {
   LOchannel.send('たいてね')
  });

  var cron = require('node-cron');
  cron.schedule('20 * * * *', () => {
   LOchannel.send('たいてたいてー')
  });

  var cron = require('node-cron');
  cron.schedule('50 * * * *', () => {
   LOchannel.send('たいて！交代10分前！')
  });

 // 〇〇分にシフト交代・リマインド等　　終わり-------------------------------------------------↑
  
 client.on('messageCreate', async message => {

 //部屋番変更
  if (message.content.match(/^[0-9]{5}$/)) {
   RoomNumberChannel.setName('部屋番号【'+message.content +'】');

   /*
   message.channel.setName('部屋番号【'+message.content +'】')
   */
   const reply = await message.channel.send(';部屋番号が変わったよ')
  }
  if (message.content.match(/^[0-9]{6}$/)) {
   RoomNumberChannel.setName('アフライ【'+message.content +'】');

   /*
   message.channel.setName('部屋番号【'+message.content +'】')
   */
   const reply = await message.channel.send(';アフライの部屋番号が変わったよ')
  }
  //部屋番変更終了

 });



 //　おみくじ機能　-----------------[確率変更はa～f]------------------------------↓
 const a = 5;
 const b = 20;
 const c = 25;
 const d = 25;
 const e = 15;
 const f = 10;

 client.on('messageCreate', message =>{
   if (message.author.id == client.user.id || message.author.bot){
     return;
   }
   if (message.content.match(/^!omikuji/)){
     let arr = [";大吉だよ！", ";中吉！", ";末吉だと思う", ";吉かな", ";残念、凶です", ";大凶、もう寝よう"];
     //let weight = [5, 25, 30, 20, 10, 10];
     let weight = [a, b, c, d, e, f];
     lotteryByWeight(message.channel.id, arr, weight);
   }
   if (message.content.match(/^;!omikuji/)){
     let arr = [";大吉だよ！", ";中吉！", ";末吉だと思う", ";吉かな", ";残念、凶です", ";大凶、もう寝よう"];
      //let weight = [5, 25, 30, 20, 10, 10];
     let weight = [a, b, c, d, e, f];
     lotteryByWeight(message.channel.id, arr, weight);
    }
  });
  client.on('messageCreate', async message => {
    if (message.content === '!kakuritsu') {
      const reply = await message.channel.send('; \n大吉：5% \n中吉：20% \n末吉：25% \n吉　：25% \n凶　：15% \n大凶：10%')
    }
    if (message.content === ';!kakuritsu') {
      const reply = await message.channel.send('; \n大吉：5% \n中吉：20% \n末吉：25% \n吉　：25% \n凶　：15% \n大凶：10%')
    }
  });


 //おみくじ機能　終了-------------------------------------------------------------↑
  
 //話題機能---------------------------------------------------------------------------------------------------------------------------------------------↓
 const aa = 10; //1
 const bb = 10; //2
 const cc = 10; //3
 const dd = 10; //4
 const ee = 10; //5
 const ff = 10; //6
 const gg = 10; //7
 const hh = 10; //8
 const ii = 10; //9
 const jj = 5;  //10
 const kk = 5;  //11

 client.on('messageCreate', message =>{
   if (message.author.id == client.user.id || message.author.bot){
     return;
   }
   if (message.content.match(/^!wadai/)){
     let arr = [";ごはんの話しよ！何たべたい？", ";みんなの好きな曲教えてほしいな", ";お菓子なにがすき？", ";推しの好きなところ3つ言って！", ";最近うれしかったことって何？", ";100万円手に入れたら何につかう？(※貯金はだめだよ！！)", ";旅行するならどこに行きたい？",";好きなプロセカのカードイラストは？",";昨日の晩御飯思い出せる？思い出せたらすごい！思い出せなかったら反省してね",";願いが1つ叶うなら何を願う？",";自分で考えろ"];
     //let weight = [5, 25, 30, 20, 10, 10];
     let weight = [aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk];
     lotteryByWeight(message.channel.id, arr, weight);
   }
   if (message.content.match(/^;!wadai/)){
     let arr = [";ごはんの話しよ！何たべたい？", ";みんなの好きな曲教えてほしいな", ";お菓子なにがすき？", ";推しの好きなところ3つ言って！", ";最近うれしかったことって何？", ";100万円手に入れたら何につかう？(※貯金はだめだよ！！)", ";旅行するならどこに行きたい？",";好きなプロセカのカードイラストは？",";昨日の晩御飯思い出せる？思い出せたらすごい！思い出せなかったら反省してね",";願いが1つ叶うなら何を願う？",";自分で考えろ"];
     //let weight = [5, 25, 30, 20, 10, 10];
     let weight = [aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk];
     lotteryByWeight(message.channel.id, arr, weight);
   }
  });

 //話題機能　終了---------------------------------------------------------------------------------------------------------------------------------------↑
  client.on('messageCreate', async message => {
    if (message.content === '!kona help') {
      const reply = await message.channel.send(';コマンド一覧\n[試験コマンド]\n!kona d　または　;!kona d\n　→botが動くかどうか確認できる\n　　　(返事なければ動かない)\n!kona t　または　;!kona t\n　→単発で炊き通知を入れられる\n\n[おみくじコマンド]\n!omikuji　または　;!omikuji\n　→おみくじが引ける\n!kakuritsu　または　;!kakuritsu\n　→おみくじの確率一覧\n\n[その他　助けてこなちゃん]\n!kona help　または　;!kona help\n　→このヘルプを出す')
    }
    if (message.content === ';!kona help') {
      const reply = await message.channel.send(';コマンド一覧\n[試験コマンド]\n!kona d　または　;!kona d\n　→botが動くかどうか確認できる\n　　　(返事なければ動かない)\n!kona t　または　;!kona t\n　→単発で炊き通知を入れられる\n\n[おみくじコマンド]\n!omikuji　または　;!omikuji\n　→おみくじが引ける\n!kakuritsu　または　;!kakuritsu\n　→おみくじの確率一覧\n\n[その他　助けてこなちゃん]\n!kona help　または　;!kona help\n　→このヘルプを出す')
    }
    if (message.content === ';!kona d') {
      const reply = await message.channel.send(';動作okだよ')
    }
    if (message.content === '!kona d') {
      const reply = await message.channel.send(';動作okだよ')
    }
    if (message.content === '!kona t') {
      const reply = await message.channel.send('たいてたいてー！')
    }
    if (message.content === ';!kona t') {
      const reply = await message.channel.send('たいてたいてー！')
    }
  })

 //サブ機能---------

 client.on('messageCreate', async message => {
    let konatime = 0;
    if (message.content === '!kona s') {
     konatime = 1;
     const reply = await message.channel.send(';時報開始するよ')
    }
    if(message.content === '!kona e'){
     konatime = 2;
     const reply = await message.channel.send(';時報終了するよ')
    }


   if(konatime == 1){  
     var cron = require('node-cron');
     cron.schedule('5 * * * *', () => {
       LOchannel.send('たいてね')
      });
    }
   if(konatime == 1){
     var cron = require('node-cron');
     cron.schedule('35 * * * *', () => {
       LOchannel.send('たいてね')
      });
    }
    if(konatime == 1){
     var cron = require('node-cron');
     cron.schedule('20 * * * *', () => {
       LOchannel.send('たいてたいてー')
      });
    }
    if(konatime == 1){
     var cron = require('node-cron');
     cron.schedule('50 * * * *', () => {
       LOchannel.send('たいて！交代10分前！')
      });
    }
  })

 //サブ機能　終了----

 function lotteryByWeight(channelId, arr, weight){
  let totalWeight = 0;
  for (var i = 0; i < weight.length; i++){
    totalWeight += weight[i];
  }
  let random = Math.floor(Math.random() * totalWeight);
  for (var i = 0; i < weight.length; i++){
    if (random < weight[i]){
      sendMsg(channelId, arr[i]);
      return;
    }else{
      random -= weight[i];
    }
  }
  console.log("lottery error");
 }

 /* 
  client.on('messageCreate', async message => {
    if (message.content === ';こ、こんにちは') {
      const reply = await message.channel.send(';<:15_kohane_3:1101133951252308028>')
      await message.react('<:15_kohane_3:1101133951252308028>')
      }
  })
 client.on('messageCreate', async message => {
    if (message.content === 'こ、こんにちは') {
      const reply = await message.channel.send(';こ、こんにちは')
      await message.react('<:15_kohane_3:1101133951252308028>')
    }
  })
 client.on('messageCreate', async message => {
    if (message.content === ';こ、こんにちは') {
      const reply = await message.channel.send(';<:15_kohane_3:1101133951252308028>')
      await message.react('<:15_kohane_3:1101133951252308028>')
      }
  })
  */
  
});




/* ------------------------------------------------------------------------------------------------------------- */

client.on('messageCreate', message =>{
  if (message.author.id == client.user.id || message.author.bot){
    return;
  }

});




function lotteryByWeight(channelId, arr, weight){
  let totalWeight = 0;
  for (var i = 0; i < weight.length; i++){
    totalWeight += weight[i];
  }
  let random = Math.floor(Math.random() * totalWeight);
  for (var i = 0; i < weight.length; i++){
    if (random < weight[i]){
      sendMsg(channelId, arr[i]);
      return;
    }else{
      random -= weight[i];
    }
  }
  console.log("lottery error");
}


if(process.env.DISCORD_BOT_TOKEN == undefined){
console.log('DISCORD_BOT_TOKENが設定されていません。');
process.exit(0);
}

client.login( process.env.DISCORD_BOT_TOKEN );

function sendReply(message, text){
 message.reply(text)
   .then(console.log("リプライ送信: " + text))
   .catch(console.error);
}

  function sendMsg(channelId, text, option={}) {
 client.channels.cache.get(channelId).send(text, option)
   .then(console.log("メッセージ送信: " + text + JSON.stringify(option)))
   .catch(console.error);
}
