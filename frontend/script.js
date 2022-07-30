'use strict';

const THEME_NAME = 'light-theme';

const html = {
    'chat-list': document.getElementById('chat-list')
};

// TODO:
class Chat {
    constructor(
        picture = null,  // link
        messengers = [],  // Discord, Telegram, VK, Email
        name = null,
        isVerified = false,
        type = null,  // 'Bot', 'Group', 'Public'
        time = '',
        status = null,  // 'Read', 'Unread', 'Error'
        mediaList = [],
        author = null,
        messageType = null,  // 'Voice message', 'Video message', 'Sticker', 'Poll', 'Photo', 'Video'
        text = null,
        isReaction = false,
        isMention = false,
        newMessages = 0
    ) {
        this._chat_ = document.createElement('button');
        this._chat_.className = 'chat';

        this.setPicture(picture);

        messengers.forEach(messenger => this.addMessengerIcon(messenger));
        this.setName(name);
        this.setVerification(isVerified);
        this.setType(type);
        this.setTime(time);

        this.setStatus(status);
        this.setMedia(mediaList);
        this.setAuthor(author);
        this.setMessageType(messageType);
        this.setText(text);
        this.setReaction(isReaction);
        this.setMention(isMention);
        // newMessages
    }

    setPicture(picture) {
        this._chat_.appendChild(document.createElement('div'));
        this._chat_.childNodes[0].className = 'chat-picture';
    }

    addMessengerIcon(messenger) { }

    removeMessengerIcon(messenger) { }

    setName(name) { }

    setVerification(isVerified) { }

    setType(type) { }

    setStatus(status) { }

    setMedia(mediaList) {
        mediaList = mediaList.slice(0, 3);

        mediaList.forEach(preview => {
        });
    }

    setAuthor(author) { }

    setMessageType(messageType) { }

    setText(text) { }

    setReaction(isReaction) { }

    setMention(isMention) { }
}


async function applyTheme(themeName) {
    await fetch(`./themes/${themeName}.json`)
        .then(response => {
            return response.json();
        })
        .then(data => {
            for (const [key, value] of Object.entries(data)) {
                document.documentElement.style.setProperty(`--${key}`, value);
            }
        });
}

applyTheme(THEME_NAME);
