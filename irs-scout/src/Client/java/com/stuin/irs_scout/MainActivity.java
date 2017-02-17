package com.stuin.irs_scout;

import android.app.Activity;
import android.content.Context;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.FrameLayout;
import android.widget.RadioButton;
import android.widget.TextView;

import java.util.List;


public class MainActivity extends Activity {
    private PageManager form;

    static String address;
    static String position;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        //Start app
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        getActionBar().hide();

        //Retrieve last ip
        address = getPreferences(Context.MODE_PRIVATE).getString("Address", getResources().getString(R.string.form_ip));
        TextView textView = (TextView) findViewById(R.id.AddressBar);
        textView.setText(address);
    }

    public void position(View view) {
        //Get tablet position
        TextView textView = (TextView) view;
        position = textView.getText().toString();

        //Get server address
        textView = (TextView) findViewById(R.id.AddressBar);
        address = textView.getText().toString();

        //Check connection
        class Connected extends Next {
            public void run(List<String> s) {
                connected();
            }
        }
        new Request("",new Connected());
    }

    private void connected() {
        //Save correct address
        SharedPreferences.Editor editor = getPreferences(Context.MODE_PRIVATE).edit();
        editor.putString("Address", address);
        editor.apply();

        //Hide start screen
        findViewById(R.id.AddressBar).setVisibility(View.GONE);
        findViewById(R.id.gridLayout).setVisibility(View.GONE);

        //Start
        form = new PageManager(this);
        FrameLayout frameLayout = (FrameLayout) findViewById(R.id.Frame);
        frameLayout.setVisibility(View.VISIBLE);
        frameLayout.addView(form);
    }

    @Override
    public void onBackPressed() {

    }

    public void nextPage(View view) {
        //Next page button
        form.nextPage(view);
    }

    public void lastPage(View view) {
        //Previous page button
        form.lastPage(view);
    }
}
