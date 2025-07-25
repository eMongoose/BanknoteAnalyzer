// See https://github.com/react-native-image-picker/react-native-image-picker?tab=readme-ov-file#options for documentation on camera functions
import ParallaxScrollView from '@/components/ParallaxScrollView';
import { ThemedText } from '@/components/ThemedText';
import { ThemedView } from '@/components/ThemedView';
import { Image } from 'expo-image';
import { useState } from 'react';
import {
  Platform,
  Pressable,
  StyleSheet,
} from 'react-native';
import {
  CameraOptions,
  ImageLibraryOptions,
  launchCamera,
  launchImageLibrary
} from 'react-native-image-picker';
import { Double } from 'react-native/Libraries/Types/CodegenTypes';

const API_BASE = "http://192.168.68.55:5000"

///////////////////////////////////////////////////////////////////////////////////////////////////
interface coinDataInterface {
  name: String
  currency: String
  value: Double
}

export default function HomeScreen() {
  // state declarations
  const [img, setImg] = useState<string | null>(null);
  const [isVisible, setIsVisible] = useState(true);
  const [coinData, setCoinData] = useState<coinDataInterface | null>(null);

  const toggleVisibility = () => {
    setIsVisible(!isVisible);
  };

  /////////////////////////////////////////////////////////////////////////////////////////////////
  /* 
    openCamera: opens the user's camera for image selection
    openLibrary: open the user's library for image selection
  */
  const openCamera = async () => {
    const options: CameraOptions = {
      mediaType: 'photo',
      quality: 1,
      saveToPhotos: false,
    };
    const result = await launchCamera(options);
    if (result.didCancel) {
      console.log("No image was selected.")
    }
    else if (result.errorCode) {
      console.log(result.errorMessage);
    }
    else if (result.assets && result.assets.length > 0) { // success
      const img = result.assets[0].uri;
      console.log("Image URI: ", img);
      setImg(img ?? null); // if img is undefined, setImg = NULL
    }
    else {
      console.log("Error: ", result);
    }
  }

  const openLibrary = async () => {
    const options: ImageLibraryOptions = {
      mediaType: 'photo',
      quality: 1,
      selectionLimit: 1,
    };
    const result = await launchImageLibrary(options);
    if (result.didCancel) {
      console.log("No image was selected")
    }
    else if (result.errorCode) {
      console.log(result.errorMessage);
    }
    else if (result.assets && result.assets.length > 0) { // success
      const img = result.assets[0].uri;
      console.log("Image URI: ", img);
      setImg(img ?? null); // if img is undefined, setImg = NULL
    }
    else {
      console.log("Error: ", result);
    }
  }
  /////////////////////////////////////////////////////////////////////////////

  const analyzeCoin = async () => {
    console.log("Analyzing the image...");

    // error  handling
    if (!img) {
      console.log("Error 1: There is no image selected!")
      return;
    }

    try {
      // https://developer.mozilla.org/en-US/docs/Web/API/FormData
      // build a formdata object
      const form = new FormData();
      const fileName = img.split('/').pop() ?? `coin_${Date.now()}.jpg`; // clean up the path to get the filename
      const ext = fileName.split('.').pop()?.toLowerCase(); // cleanup the filename to get the MIME extension

      // file of MIME type (image, jpeg, etc.)
      const mime =
        ext === 'png' ? 'image/png' :
          ext === 'heic' ? 'image/heic' :
            'image/jpeg';

      // append it to the formdata
      // https://developer.mozilla.org/en-US/docs/Web/API/FormData/append
      if (Platform.OS === 'web') {
        // Fetch the blob from the web URL
        const response = await fetch(img);
        const blob = await response.blob();

        form.append('image', new File([blob], fileName, { type: mime }));
      } else {
        // Native (iOS/Android)
        form.append('image', {
          uri: img,
          name: fileName,
          type: mime,
        } as any);
      }

      // fetch and send formdata to the server
      const response = await fetch(`${API_BASE}/getCoin`, {
        method: 'POST',
        body: form,
        headers: { Accept: 'application/json', },
      });

      // error handling
      if (!response.ok) {
        throw new Error("Error 2");
      }

      const json: coinDataInterface = await response.json();
      setCoinData(json);
      // console.log("Data: ", json);
    }
    catch (error) {
      console.log("Error 3: ", error);
    }
  };
  /////////////////////////////////////////////////////////////////////////////////////////////////
  // main function
  return (
    <ParallaxScrollView
      headerBackgroundColor={{ light: '#A1CEDC', dark: '#ffffffff' }}
      headerImage={<Image style={styles.banner} source={require('@/assets/images/partial-react-logo.png')} />}>

      <ThemedView style={{ height: 500 }}>
        {/* Title: Coin Identifier*/}
        <ThemedView style={styles.titleContainer}>
          <ThemedText type="title">Coin Identifier</ThemedText>
        </ThemedView>

        {isVisible ?
          <ThemedView style={{ position: 'absolute', bottom: 0, left: 0, right: 0 }}>
            <ThemedView style={{ flexDirection: 'row', justifyContent: 'space-between', width: '80%', margin: 'auto', gap: 8 }}>
              <Pressable style={styles.pictureButton} onPress={openCamera}>
                <ThemedText style={styles.pictureButtonText}>Take Picture</ThemedText>
              </Pressable>
              <Pressable style={styles.pictureButton} onPress={openLibrary}>
                <ThemedText style={styles.pictureButtonText}>Select a picture</ThemedText>
              </Pressable>
            </ThemedView>
          </ThemedView>
          : null
        }

        {/* Result */}
        {img && (
          <ThemedView style={styles.imageContainer}>
            <Image
              style={{ height: '100%', width: '100%' }}
              source={{ uri: img }}
              contentFit="contain"
              onLoadEnd={() => {
                toggleVisibility();
              }}
            />
          </ThemedView>
        )}
        {/* Use this picture */}
        {/* There's probably a better way of doing this lol*/}
        {img && (
          <ThemedView style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
            <ThemedView style={{ margin: 'auto' }}>
              <Pressable style={styles.retakeButtonContainer} onPress={analyzeCoin}>
                <ThemedText style={styles.pictureButtonText}>Analyze Coin</ThemedText>
              </Pressable>
            </ThemedView>
            <ThemedText style={{ textAlign: 'center', fontWeight: 500 }}>OR</ThemedText>
            <ThemedView>
              <ThemedView style={{ flexDirection: 'row', justifyContent: 'space-between', width: '80%', margin: 'auto' }}>
                <Pressable style={styles.pictureButton} onPress={openCamera}>
                  <ThemedText style={styles.pictureButtonText}>Retake Picture</ThemedText>
                </Pressable>
                <Pressable style={styles.pictureButton} onPress={openLibrary}>
                  <ThemedText style={styles.pictureButtonText}>Select a picture</ThemedText>
                </Pressable>
              </ThemedView>
            </ThemedView>
          </ThemedView>
        )}
      </ThemedView>
    </ParallaxScrollView >
  );
}

const styles = StyleSheet.create({
  banner: {
    height: '100%',
    width: '100%',
  },

  titleContainer: {
    flexDirection: 'row',
    alignItems: 'center',
  },

  pictureButton: {
    borderWidth: 1.5,
    borderRadius: 20,
    alignItems: 'center',
    paddingLeft: 20,
    paddingRight: 20,
    paddingTop: 10,
    paddingBottom: 10,
    minWidth: 150,
    backgroundColor: 'white',
    cursor: 'pointer',
  },

  pictureButtonText: {
    color: 'black',
    fontWeight: 700,
  },

  imageContainer: {
    height: 300,
    width: 300,
    margin: 'auto',
  },

  retakeButtonContainer: {
    borderWidth: 1.5,
    borderRadius: 20,
    alignItems: 'center',
    paddingLeft: 20,
    paddingRight: 20,
    paddingTop: 10,
    paddingBottom: 10,
    width: 200,
    backgroundColor: 'white',
    cursor: 'pointer',
  }
});
