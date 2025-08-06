// See https://github.com/react-native-image-picker/react-native-image-picker?tab=readme-ov-file#options for documentation on camera functions
import ParallaxScrollView from '@/components/ParallaxScrollView';
import { ThemedText } from '@/components/ThemedText';
import { ThemedView } from '@/components/ThemedView';
import { Image } from 'expo-image';
import { useState } from 'react';
import {
  Modal,
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
import { EXPO_PUBLIC_API_URL } from '@env';

export const API_BASE = EXPO_PUBLIC_API_URL;

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
  const [modalVisible, setModalVisible] = useState(false);

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
    if (!img) {
      console.log("Error 1: There is no image selected!")
      return;
    }
    // https://developer.mozilla.org/en-US/docs/Web/API/FormData
    // build a formdata object
    const form = new FormData();
    const fileName = img.split('/').pop() || `coin_${Date.now()}.jpg`; // clean up the path to get the filename
    const ext = fileName.split('.').pop()?.toLowerCase(); // cleanup the filename to get the MIME extension
    const mime = ext === 'png' // file of MIME type (image, jpeg, etc.)
      ? 'image/png'
      : ext === 'heic'
        ? 'image/heic'
        : 'image/jpeg';

    // append it to the formdata
    // https://developer.mozilla.org/en-US/docs/Web/API/FormData/append
    if (Platform.OS === 'web') {
      const imageResponse = await fetch(img);
      const blob = await imageResponse.blob();
      form.append('image', new File([blob], fileName, { type: mime }));
    }
    else {
      form.append('image', {
        uri: img,
        name: fileName,
        type: mime,
      } as any);
    }
    // fetch and send formdata to the server
    try {
      const response = await fetch(`${API_BASE}/getCoin`, {
        method: 'POST',
        body: form,
        headers: { Accept: 'application/json', },
      });
      if (!response.ok) {
        const err = await response.json().catch(() => ({}));
        throw new Error(err.error || `HTTP ${response.status}`);
      }
      const json = await response.json();
      setCoinData(json);
      setModalVisible(true);
    } catch (err) {
      console.error("Analyze failed:", err);
    };
  }
  /////////////////////////////////////////////////////////////////////////////////////////////////
  // main function
  return (
    <ParallaxScrollView
      headerBackgroundColor={{ light: '#A1CEDC', dark: '#ffffffff' }}
      headerImage={<Image style={styles.banner} source={require('@/assets/images/banner.png')} />}>

      <ThemedView style={{ height: 500 }}>
        {/* Title: Coin Identifier*/}
        <ThemedView style={styles.titleContainer}>
          <ThemedText type="title">Coin Identifier</ThemedText>
        </ThemedView>

        {isVisible ?
          <ThemedView style={{ position: 'absolute', bottom: 0, left: 0, right: 0 }}>
            <ThemedView style={{ display: 'flex', flexDirection: 'row', gap: 10, width: '60%', justifyContent: 'space-around', margin: 'auto' }}>
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
        {img && (
          <ThemedView style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
            <ThemedView style={{ margin: 'auto' }}>
              <Pressable style={styles.retakeButtonContainer} onPress={analyzeCoin}>
                <ThemedText style={styles.pictureButtonText}>Analyze Coin</ThemedText>
              </Pressable>
            </ThemedView>
            <ThemedText style={{ textAlign: 'center', fontWeight: 500 }}>OR</ThemedText>
            <ThemedView>
              <ThemedView style={{ display: 'flex', flexDirection: 'row', gap: 10, width: '60%', justifyContent: 'space-around', margin: 'auto' }}>
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

        {/* Popup */}
        <Modal
          transparent={true}
          visible={modalVisible}
        >
          <ThemedView style={styles.centeredView}>
            <ThemedView style={styles.modalView}>
              <ThemedText style={styles.modalTitle}>Coin Results:</ThemedText>

              {/* POPUP CONTENTS HERE */}
              <ThemedView style={styles.resultsTextContainer}>
                <ThemedText style={styles.resultsText}>This coin is predicted to be a {coinData?.name}</ThemedText>
                <ThemedText style={styles.resultsText}>The coin's value is {coinData?.value}</ThemedText>
              </ThemedView>
              {/* CLOSE BUTTON */}
              <Pressable
                style={styles.buttonClose}
                onPress={() => setModalVisible(!modalVisible)}>
                <ThemedText style={styles.textStyle}>Close</ThemedText>
              </Pressable>
            </ThemedView>
          </ThemedView>
        </Modal>

        {/* END OF TAG */}
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
  },

  /*****************************************************/
  centeredView: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: 'rgba(0, 0, 0, 0.80)',
  },
  modalView: {
    margin: 20,
    backgroundColor: 'white',
    borderRadius: 20,
    padding: 35,
    alignItems: 'center',
    shadowColor: '#000',
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.25,
    shadowRadius: 4,
    elevation: 5,
    gap: 25,
    paddingLeft: 100,
    paddingRight: 100
  },

  buttonClose: {
    borderRadius: 20,
    paddingLeft: 20,
    paddingRight: 20,
    paddingTop: 5,
    paddingBottom: 5,
    elevation: 2,
    backgroundColor: '#2196F3',
  },

  textStyle: {
    color: 'white',
    fontWeight: 'bold',
    textAlign: 'center',
  },

  modalTitle: {
    marginBottom: 15,
    textAlign: 'center',
    color: 'black'
  },

  /************************************/
  resultsTextContainer: {
    display: 'flex',
    flexDirection: 'column',
    gap: 10,
    backgroundColor: 'white'
  },

  resultsText: {
    textAlign: 'center',
    color: 'black'
  }
});
