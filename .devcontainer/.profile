# ~/.profile: executed by Bourne-compatible login shells.

if [ "$BASH" ]; then
  if [ -f ~/.bashrc ]; then
    . ~/.bashrc
  fi
fi

if [ "$ZSH" ]; then
  if [ -f ~/.zshrc ]; then
    . ~/.zshrc
  fi
fi

mesg n || true