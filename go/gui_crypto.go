package main

import (
	"fmt"
	"strings"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/layout"
	"fyne.io/fyne/v2/widget"
)

// ALPHABET provides the letter order for Caesar and Vigenere.
const ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

// caesarBreak returns all 26 Caesar shift attempts for the given text.
func caesarBreak(text string) string {
	text = strings.ToUpper(text)
	var lines []string
	for shift := 0; shift < 26; shift++ {
		var out strings.Builder
		for _, ch := range text {
			idx := strings.IndexRune(ALPHABET, ch)
			if idx >= 0 {
				// rotate alphabet backwards by shift
				idx = (idx - shift + 26) % 26
				out.WriteByte(ALPHABET[idx])
			} else {
				out.WriteRune(ch)
			}
		}
		lines = append(lines, fmt.Sprintf("%2d: %s", shift, out.String()))
	}
	return strings.Join(lines, "\n")
}

// vigenereDecrypt performs classic Vigenere decryption using key letters as shifts.
func vigenereDecrypt(text, key string) string {
	if key == "" {
		return "⚠️  Key required for Vigenère"
	}
	text = strings.ToUpper(text)
	key = strings.ToUpper(key)
	keyLen := len(key)
	var out strings.Builder
	k := 0
	for _, ch := range text {
		idx := strings.IndexRune(ALPHABET, ch)
		if idx >= 0 {
			shift := strings.IndexRune(ALPHABET, rune(key[k]))
			idx = (idx - shift + 26) % 26
			out.WriteByte(ALPHABET[idx])
			k = (k + 1) % keyLen
		} else {
			out.WriteRune(ch)
		}
	}
	return out.String()
}

func main() {
	// Create the application window.
	a := app.New()
	w := a.NewWindow("Simple Cipher Helper")

	// ---- Widgets ----

	// radio buttons choose the cipher
	cipher := widget.NewRadioGroup([]string{"Caesar (show all shifts)", "Vigenère"}, nil)
	cipher.SetSelected("Caesar (show all shifts)")

	// key entry - used only for Vigenere
	keyEntry := widget.NewEntry()

	// text input for the ciphertext
	textBox := widget.NewMultiLineEntry()
	textBox.SetPlaceHolder("Enter ciphertext here")

	// output area is read-only
	outBox := widget.NewMultiLineEntry()
	outBox.Disable()

	// button to run decryption
	runBtn := widget.NewButton("Decrypt / Break", func() {
		txt := strings.TrimSpace(textBox.Text)
		if txt == "" {
			outBox.SetText("Please enter ciphertext first")
			return
		}
		if cipher.Selected == "Caesar (show all shifts)" {
			outBox.SetText(caesarBreak(txt))
		} else {
			outBox.SetText(vigenereDecrypt(txt, strings.TrimSpace(keyEntry.Text)))
		}
	})

	// clear button resets text fields
	clearBtn := widget.NewButton("Clear", func() {
		textBox.SetText("")
		outBox.SetText("")
	})

	// hide or show key entry depending on cipher choice
	cipher.OnChanged = func(s string) {
		if s == "Vigenère" {
			keyEntry.Enable()
		} else {
			keyEntry.Disable()
		}
	}
	cipher.OnChanged(cipher.Selected) // set initial state

	// layout using vertical boxes like nodes stacked together
	w.SetContent(container.NewVBox(
		container.New(layout.NewFormLayout(), widget.NewLabel("Cipher:"), cipher),
		container.New(layout.NewFormLayout(), widget.NewLabel("Key:"), keyEntry),
		widget.NewLabel("Ciphertext:"), textBox,
		container.NewHBox(runBtn, clearBtn),
		widget.NewLabel("Output:"), outBox,
	))

	w.Resize(fyne.NewSize(600, 400))
	w.ShowAndRun()
}
